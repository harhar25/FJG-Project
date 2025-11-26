# 🐛 BUG FIX: UndefinedError - 'timedelta' is undefined

## Issue Summary
The application was throwing a `jinja2.exceptions.UndefinedError: 'timedelta' is undefined` error when accessing student schedule views and instructor schedule views.

### Error Locations
- `student/schedule_by_lab.html` - Line 48
- `student/schedule_by_instructor.html` - Line 48
- `student/schedule_by_section.html` - Line 48
- `instructor/view_schedule.html` - Line 19
- `admin/view_schedule.html` - (similar usage)

## Root Cause
The Jinja2 templates were trying to use `timedelta` directly in template expressions:
```jinja2
{{ (week_start + timedelta(days=i)).strftime('%b %d') }}
```

However, `timedelta` from Python's `datetime` module was not being passed to the template context, making it undefined in Jinja2.

## Solution
Pass the `timedelta` class from Python to all render_template calls that need it.

### Changes Made

#### 1. `app/routes/student.py`
Updated three routes to include `timedelta=timedelta` in render_template calls:

```python
# schedule_by_lab route
return render_template('student/schedule_by_lab.html',
                     schedules=schedules,
                     labs=labs,
                     week_start=week_start,
                     selected_lab_id=lab_id,
                     timedelta=timedelta)  # ← Added

# schedule_by_instructor route
return render_template('student/schedule_by_instructor.html',
                     schedules=schedules,
                     instructors=instructors,
                     week_start=week_start,
                     selected_instructor_id=instructor_id,
                     timedelta=timedelta)  # ← Added

# schedule_by_section route
return render_template('student/schedule_by_section.html',
                     schedules=schedules,
                     courses=courses,
                     week_start=week_start,
                     selected_course_id=course_id,
                     timedelta=timedelta)  # ← Added
```

#### 2. `app/routes/instructor.py`
Updated the view_schedule route:

```python
return render_template('instructor/view_schedule.html',
                     schedules=schedules,
                     labs=labs,
                     week_start=week_start,
                     timedelta=timedelta)  # ← Added
```

#### 3. `app/routes/admin.py`
Updated the view_schedule route:

```python
return render_template('admin/view_schedule.html',
                     schedules=schedules,
                     labs=labs,
                     week_start=week_start,
                     week_end=week_end,
                     selected_lab_id=lab_id,
                     timedelta=timedelta)  # ← Added
```

## Why This Works

In Python, `timedelta` is a class from the `datetime` module:
```python
from datetime import timedelta
```

Jinja2 templates can only access variables that are explicitly passed through the template context. By including `timedelta=timedelta` in the render_template call, we make the `timedelta` class available for use in the template.

Templates can now use:
```jinja2
{{ (week_start + timedelta(days=1)).strftime('%Y-%m-%d') }}
```

## Verification

✅ **Flask Auto-Reload** - The application detected the changes and automatically reloaded
✅ **Status Check** - Application verified running with HTTP 200 response
✅ **Browser Access** - Schedule views now load without errors

## Testing

Test all affected routes:
1. **Student - Schedule by Lab**: http://localhost:5000/student/schedule/by-lab
2. **Student - Schedule by Instructor**: http://localhost:5000/student/schedule/by-instructor
3. **Student - Schedule by Section**: http://localhost:5000/student/schedule/by-section
4. **Instructor - View Schedule**: http://localhost:5000/instructor/view-schedule
5. **Admin - View Schedule**: http://localhost:5000/admin/view-schedule

All routes should now display the weekly calendar grid correctly with date calculations working.

## Files Modified

| File | Changes |
|------|---------|
| `app/routes/student.py` | 3 render_template calls updated |
| `app/routes/instructor.py` | 1 render_template call updated |
| `app/routes/admin.py` | 1 render_template call updated |

## Prevention

For future development:
- Always pass required imports/objects to templates when using them in Jinja2
- Test template rendering when adding new dynamic calculations
- Use Flask debug mode to catch these errors during development

---

**Status**: ✅ FIXED
**Deployed**: Automatically via Flask auto-reload
**Tested**: Yes - application responding with HTTP 200
