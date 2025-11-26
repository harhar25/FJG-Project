# 📋 HTML MODERNIZATION GUIDE - EXACT CHANGES NEEDED

## Quick Reference: Before & After Examples

### TABLE PAGE EXAMPLE (manage_labs.html)

#### BEFORE (Current - Basic Bootstrap)
```html
<div class="container-fluid">
    <div class="row mb-4">
        <div class="col-12">
            <h1 class="h2">
                <i class="fas fa-flask-vial"></i> Manage Laboratory Rooms
            </h1>
        </div>
    </div>
    
    <div class="card shadow">
        <div class="table-responsive">
            <table class="table table-hover mb-0">
                <thead class="table-light">
                    <tr>
                        <th>Lab Code</th>
                        <th>Lab Name</th>
                        <!-- ... -->
                    </tr>
                </thead>
                <tbody>
                    <!-- rows -->
                </tbody>
            </table>
        </div>
    </div>
</div>
```

#### AFTER (Modern - With Design System)
```html
<div class="container-modern">
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">
                <i class="fas fa-flask-vial"></i> Manage Laboratory Rooms
            </h1>
            <p class="hero-subtitle">Create, edit, and manage all laboratory facilities</p>
        </div>
    </div>

    <!-- Stat Cards (Optional) -->
    <div class="grid-responsive mb-4">
        <div class="stat-card">
            <div class="stat-card-icon">
                <i class="fas fa-flask"></i>
            </div>
            <div class="stat-card-value">12</div>
            <div class="stat-card-label">Total Labs</div>
        </div>
        <!-- More stats -->
    </div>

    <!-- Action Button -->
    <div class="mb-4">
        <button class="btn-modern btn-modern-primary" data-bs-toggle="modal" data-bs-target="#addLabModal">
            <i class="fas fa-plus"></i> Add New Lab
        </button>
    </div>

    <!-- Modern Card Wrapper -->
    <div class="card-modern">
        <div class="card-modern-header">
            <h5>Laboratory Directory</h5>
        </div>
        <div class="card-modern-body">
            <div class="table-responsive">
                <table class="table table-striped table-hover mb-0">
                    <thead>
                        <tr>
                            <th>Lab Code</th>
                            <th>Lab Name</th>
                            <th>Capacity</th>
                            <th>Location</th>
                            <th>Equipment</th>
                            <th class="text-center">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for lab in labs.items %}
                        <tr>
                            <td>
                                <span class="badge bg-primary">{{ lab.lab_code }}</span>
                            </td>
                            <td>{{ lab.lab_name }}</td>
                            <td>
                                <span class="badge bg-info">{{ lab.capacity }}</span>
                            </td>
                            <td>{{ lab.location }}</td>
                            <td>
                                <small class="text-muted">{{ lab.equipment[:30] }}...</small>
                            </td>
                            <td class="text-center">
                                <button class="btn-modern btn-modern-primary btn-sm">
                                    <i class="fas fa-edit"></i> Edit
                                </button>
                                <button class="btn-modern btn-modern-secondary btn-sm">
                                    <i class="fas fa-trash"></i> Delete
                                </button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
```

---

### FORM PAGE EXAMPLE (submit_request.html)

#### BEFORE (Current - Basic Bootstrap Form)
```html
<div class="container-fluid">
    <div class="row">
        <div class="col-md-8 mx-auto">
            <div class="card shadow">
                <div class="card-header bg-primary text-white">
                    <h4>Submit Lab Reservation Request</h4>
                </div>
                <div class="card-body p-4">
                    <form method="POST">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label class="form-label">Instructor Name</label>
                                <input type="text" class="form-control" disabled>
                            </div>
                        </div>
                        <!-- more fields -->
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
```

#### AFTER (Modern - With Design System)
```html
<div class="container-modern">
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="hero-content">
            <h2 class="hero-title">
                <i class="fas fa-plus-circle"></i> Lab Reservation Request
            </h2>
            <p class="hero-subtitle">Request a laboratory room for your class session</p>
        </div>
    </div>

    <!-- Main Form Card -->
    <div class="card-modern" style="max-width: 700px; margin: 0 auto;">
        <div class="card-modern-body">
            <form method="POST" id="requestForm">
                <!-- Two-column layout -->
                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label for="instructor_name" class="form-label">
                            <i class="fas fa-user"></i> Instructor Name
                        </label>
                        <input type="text" class="form-control" id="instructor_name" 
                               value="{{ current_user.full_name }}" disabled>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="course_id" class="form-label">
                            <i class="fas fa-book"></i> Course / Subject <span class="text-danger">*</span>
                        </label>
                        <select class="form-select" id="course_id" name="course_id" required>
                            <option value="">-- Select Course --</option>
                            {% for course in courses %}
                            <option value="{{ course.id }}">
                                {{ course.course_code }} - {{ course.course_name }}
                            </option>
                            {% endfor %}
                        </select>
                        <small class="form-text text-muted">Choose your course from the list</small>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label for="lab_id" class="form-label">
                            <i class="fas fa-flask"></i> Lab Room <span class="text-danger">*</span>
                        </label>
                        <select class="form-select" id="lab_id" name="lab_id" required>
                            <option value="">-- Select Lab --</option>
                            {% for lab in labs %}
                            <option value="{{ lab.id }}">
                                {{ lab.lab_code }} - {{ lab.lab_name }}
                            </option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="requested_date" class="form-label">
                            <i class="fas fa-calendar"></i> Date <span class="text-danger">*</span>
                        </label>
                        <input type="date" class="form-control" id="requested_date" 
                               name="requested_date" required>
                    </div>
                </div>

                <div class="row">
                    <div class="col-md-6 mb-3">
                        <label for="start_time" class="form-label">
                            <i class="fas fa-clock"></i> Start Time <span class="text-danger">*</span>
                        </label>
                        <input type="time" class="form-control" id="start_time" 
                               name="start_time" required>
                    </div>

                    <div class="col-md-6 mb-3">
                        <label for="end_time" class="form-label">
                            <i class="fas fa-hourglass-end"></i> End Time <span class="text-danger">*</span>
                        </label>
                        <input type="time" class="form-control" id="end_time" 
                               name="end_time" required>
                    </div>
                </div>

                <div class="mb-3">
                    <label for="reason" class="form-label">
                        <i class="fas fa-note-sticky"></i> Reason / Notes <span class="text-danger">*</span>
                    </label>
                    <textarea class="form-control" id="reason" name="reason" rows="4" 
                              required placeholder="Provide details about your lab requirements..."></textarea>
                    <small class="form-text text-muted">Maximum 500 characters</small>
                </div>

                <!-- Info Alert -->
                <div class="alert alert-modern alert-info mb-4">
                    <div style="display: flex; align-items: center; gap: 1rem;">
                        <i class="fas fa-info-circle" style="font-size: 1.5rem;"></i>
                        <div>
                            <strong>Operating Hours:</strong> Lab facilities available 8:00 AM - 7:00 PM
                        </div>
                    </div>
                </div>

                <!-- Form Actions -->
                <div class="d-flex gap-2">
                    <button type="submit" class="btn-modern btn-modern-primary">
                        <i class="fas fa-paper-plane"></i> Submit Request
                    </button>
                    <button type="reset" class="btn-modern btn-modern-secondary">
                        <i class="fas fa-redo"></i> Clear Form
                    </button>
                    <a href="{{ url_for('instructor.my_requests') }}" class="btn-modern btn-modern-secondary">
                        <i class="fas fa-arrow-left"></i> Cancel
                    </a>
                </div>
            </form>
        </div>
    </div>
</div>
```

---

### SCHEDULE GRID PAGE EXAMPLE (schedule_by_lab.html)

#### BEFORE (Current - Plain Card Grid)
```html
<div class="container-fluid">
    <div class="row mb-4">
        <div class="col-12">
            <h1 class="h2">Schedule by Lab Room</h1>
        </div>
    </div>
    
    <div class="card shadow mb-4">
        <div class="card-body">
            <!-- filters -->
        </div>
    </div>
    
    <div class="row">
        {% for i in range(7) %}
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card shadow">
                <div class="card-header bg-success text-white">
                    <h6>{{ days[i] }}</h6>
                </div>
                <div class="card-body p-0">
                    <!-- schedule items -->
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
```

#### AFTER (Modern - With Design System)
```html
<div class="container-modern">
    <!-- Hero Section -->
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">
                <i class="fas fa-calendar-alt"></i> Weekly Lab Schedule
            </h1>
            <p class="hero-subtitle">View all lab sessions by room for the selected week</p>
        </div>
    </div>

    <!-- Filter Section -->
    <div class="card-modern mb-4">
        <div class="card-modern-body">
            <div class="row g-3">
                <div class="col-md-6">
                    <label class="form-label">
                        <i class="fas fa-flask"></i> Select Lab Room
                    </label>
                    <select class="form-select" id="labFilter" onchange="filterSchedule()">
                        <option value="">All Labs</option>
                        {% for lab in labs %}
                        <option value="{{ lab.id }}" {% if selected_lab_id == lab.id %}selected{% endif %}>
                            {{ lab.lab_code }} - {{ lab.lab_name }} (Cap: {{ lab.capacity }})
                        </option>
                        {% endfor %}
                    </select>
                </div>
                <div class="col-md-6">
                    <label class="form-label">
                        <i class="fas fa-calendar"></i> Week Starting
                    </label>
                    <input type="date" class="form-control" id="weekFilter" 
                           value="{{ week_start }}" onchange="filterSchedule()">
                </div>
            </div>
        </div>
    </div>

    <!-- Weekly Schedule Grid -->
    <div class="grid-responsive">
        {% set days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] %}
        {% for i in range(7) %}
        <div>
            <div class="card-modern">
                <!-- Modern gradient header -->
                <div class="card-modern-header" style="background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);">
                    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%;">
                        <div>
                            <h6 style="margin: 0; font-weight: 700;">{{ days[i] }}</h6>
                            <small style="opacity: 0.9;">{{ (week_start + timedelta(days=i)).strftime('%b %d, %Y') }}</small>
                        </div>
                        <div style="font-size: 1.5rem; opacity: 0.8;">
                            <i class="fas fa-calendar-day"></i>
                        </div>
                    </div>
                </div>

                <div class="card-modern-body" style="padding: 0;">
                    <div class="list-group list-group-flush">
                        {% set current_date = (week_start + timedelta(days=i)) %}
                        {% set day_schedules = schedules | selectattr('scheduled_date', 'equalto', current_date) | list %}
                        
                        {% if day_schedules %}
                            {% for schedule in day_schedules %}
                            <div class="list-group-item" style="border-left: 4px solid #6366f1; padding: 1rem;">
                                <div style="display: flex; justify-content: space-between; align-items: start;">
                                    <div style="flex: 1;">
                                        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                                            <span class="badge bg-primary">
                                                {{ schedule.start_time.strftime('%H:%M') }} - {{ schedule.end_time.strftime('%H:%M') }}
                                            </span>
                                            <span class="badge bg-success">Active</span>
                                        </div>
                                        <div style="font-weight: 600; color: #1e293b;">
                                            {{ schedule.course.course_code if schedule.course else 'N/A' }}
                                        </div>
                                        <small style="color: #64748b;">
                                            {% if schedule.course %}
                                            Section {{ schedule.course.section }} • 
                                            {{ schedule.course.instructor.full_name if schedule.course.instructor else 'Unknown Instructor' }}
                                            {% endif %}
                                        </small>
                                    </div>
                                    <div>
                                        <i class="fas fa-chevron-right" style="color: #cbd5e1;"></i>
                                    </div>
                                </div>
                            </div>
                            {% endfor %}
                        {% else %}
                        <div class="text-center" style="padding: 2rem; color: #94a3b8;">
                            <i class="fas fa-inbox" style="font-size: 2rem; margin-bottom: 0.5rem; display: block;"></i>
                            <small>No sessions scheduled</small>
                        </div>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}
    </div>
</div>
```

---

## Key CSS Classes to Use

### Card Styling
```css
.card-modern         /* Main card wrapper */
.card-modern-header  /* Header with gradient */
.card-modern-body    /* Content area with padding */
```

### Layout
```css
.container-modern    /* Max-width container */
.grid-responsive     /* Auto-fit grid */
.hero-section        /* Page header with gradient */
```

### Components
```css
.btn-modern              /* Modern button */
.btn-modern-primary      /* Primary button */
.btn-modern-secondary    /* Secondary button */
.stat-card               /* Stat card with icon */
.badge                   /* Status badges */
.alert-modern            /* Modern alert */
```

### Utilities
```css
.section-divider     /* Visual divider between sections */
.text-muted          /* Muted text color */
.form-label          /* Better label styling */
```

---

## Color Coding for Status Badges

### Admin Pages
```html
<!-- Lab Status -->
<span class="badge bg-success">Active</span>
<span class="badge bg-warning">Maintenance</span>
<span class="badge bg-danger">Inactive</span>

<!-- Request Status -->
<span class="badge bg-info">Pending</span>
<span class="badge bg-success">Approved</span>
<span class="badge bg-danger">Rejected</span>
```

### Instructor/Student Pages
```html
<!-- Booking Status -->
<span class="badge bg-primary">Booked</span>
<span class="badge bg-warning">Pending</span>
<span class="badge bg-danger">Cancelled</span>
```

---

## Common Patterns

### Empty State
```html
<div class="text-center" style="padding: 3rem; color: #94a3b8;">
    <i class="fas fa-inbox" style="font-size: 3rem; margin-bottom: 1rem; display: block;"></i>
    <h5>No Data Available</h5>
    <p>There are no items to display at this time.</p>
</div>
```

### Loading State
```html
<div class="skeleton-loader" style="height: 100px; border-radius: 8px;"></div>
```

### Info Alert
```html
<div class="alert-modern alert-info">
    <div style="display: flex; align-items: center; gap: 1rem;">
        <i class="fas fa-info-circle" style="font-size: 1.5rem;"></i>
        <div>Your message here</div>
    </div>
</div>
```

---

## Responsive Breakpoints to Keep in Mind

```css
Desktop (>992px)  - Full layout
Tablet (768-992px) - Adjusted spacing
Mobile (<768px)   - Stacked layout
```

All components are already responsive from **components.css** and **main-content-modern.css**.

---

This guide shows exactly what to change. Ready to upgrade the HTML files?

*Last Updated: November 26, 2025*
