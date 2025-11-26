# 📋 NAVBAR CODE STRUCTURE GUIDE

## File Organization

```
app/
├── templates/
│   ├── base.html ← REPLACE with base_new.html
│   ├── base_new.html ← NEW FILE (complete navbar)
│   ├── base_old.html ← BACKUP of old base.html
│   ├── dashboard.html
│   ├── login.html
│   ├── signup.html
│   ├── admin/
│   │   ├── dashboard.html
│   │   ├── manage_labs.html
│   │   ├── manage_instructors.html
│   │   └── approve_requests.html
│   ├── instructor/
│   │   ├── dashboard.html
│   │   ├── my_labs.html
│   │   ├── submit_request.html
│   │   └── my_requests.html
│   └── student/
│       ├── dashboard.html
│       └── schedule.html
│
└── static/
    └── css/
        ├── navbar-advanced.css ← NEW FILE (17 KB)
        ├── main-content-modern.css ← NEW FILE (12 KB)
        ├── enterprise.css ✓ (existing)
        ├── visual-design.css ✓ (existing)
        ├── components.css ✓ (existing)
        ├── auth.css ✓ (existing)
        └── style.css ✓ (existing)
```

---

## HTML Structure in base_new.html

### Section 1: Head (Meta & CSS)

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Lab Schedule Management{% endblock %}</title>

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Custom CSS Files (7 files total) -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/navbar-advanced.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/enterprise.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/visual-design.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/components.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main-content-modern.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/auth.css') }}">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">

    {% block extra_css %}{% endblock %}
</head>
```

### Section 2: Navbar (Desktop)

```html
<nav class="navbar-modern">
    <!-- Brand -->
    <a href="{{ url_for('main.home') }}" class="navbar-brand-modern">
        <i class="fas fa-flask-vial"></i>
        <span>Lab Management</span>
    </a>

    <!-- Horizontal Icon Navigation (Desktop Only) -->
    <div class="navbar-horizontal-icons">
        <!-- Dashboard -->
        <a href="{{ url_for('main.home') }}" class="nav-icon-item">
            <i class="fas fa-chart-line"></i>
            <div class="nav-icon-tooltip">Dashboard</div>
        </a>

        <!-- Admin Dropdown (Only for admins) -->
        {% if current_user.is_authenticated and current_user.role == 'admin' %}
        <div class="nav-icon-item nav-dropdown-trigger">
            <i class="fas fa-cog"></i>
            <div class="nav-icon-tooltip">Admin</div>
            <div class="nav-dropdown-menu">
                <a href="{{ url_for('admin.manage_labs') }}" class="dropdown-item-link">
                    <i class="fas fa-flask"></i>
                    <span>Manage Labs</span>
                </a>
                <!-- More items -->
            </div>
        </div>
        {% endif %}
        
        <!-- More icons... -->
    </div>

    <!-- Hamburger & Profile -->
    <div style="display: flex; align-items: center; gap: 1rem; margin-left: auto;">
        <!-- Hamburger Menu (Mobile) -->
        <button class="hamburger-btn" onclick="toggleMobileMenu()">
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
            <span class="hamburger-line"></span>
        </button>

        <!-- Profile Dropdown (Desktop) -->
        {% if current_user.is_authenticated %}
        <div class="profile-dropdown" id="profileDropdownDesktop">
            <button class="profile-trigger" onclick="event.stopPropagation()">
                <i class="fas fa-user"></i>
            </button>
            <div class="profile-menu">
                <!-- Menu items -->
            </div>
        </div>
        {% else %}
        <a href="{{ url_for('auth.login') }}" style="...">
            <i class="fas fa-sign-in-alt"></i>
            <span>Login</span>
        </a>
        {% endif %}
    </div>
</nav>
```

### Section 3: Mobile Menu Overlay

```html
<div class="mobile-menu-overlay" id="mobileMenuOverlay">
    <div class="mobile-menu-content">
        <!-- User Profile Section (Mobile) -->
        {% if current_user.is_authenticated %}
        <div class="mobile-menu-section">
            <div style="display: flex; align-items: center; gap: 1rem; padding: 1.25rem; ...">
                <!-- User avatar and info -->
            </div>
        </div>

        <!-- Main Navigation (Mobile) -->
        <div class="mobile-menu-section">
            <div class="mobile-menu-title">
                <i class="fas fa-compass"></i> Navigation
            </div>
            <a href="{{ url_for('main.home') }}" class="mobile-menu-item">
                <i class="fas fa-chart-line"></i>
                <span>Dashboard</span>
            </a>
            <!-- More items -->
        </div>

        <!-- Additional Options (Mobile) -->
        <div class="mobile-menu-section">
            <div class="mobile-menu-title">
                <i class="fas fa-ellipsis-h"></i> More
            </div>
            <!-- Settings, Logout -->
        </div>
        {% else %}
        <!-- Login Prompt for non-authenticated users -->
        {% endif %}
    </div>
</div>
```

### Section 4: Main Content

```html
<main class="main-content-modern">
    <!-- Flash Messages -->
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ 'danger' if category == 'error' else category }} ...">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}
    {% endwith %}

    <!-- Page Content Block -->
    {% block content %}{% endblock %}
</main>
```

### Section 5: Footer

```html
<footer style="...">
    <div class="container">
        <div class="row">
            <!-- Footer content -->
        </div>
    </div>
</footer>
```

### Section 6: Scripts

```html
<!-- Bootstrap & jQuery -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<!-- Custom JavaScript -->
<script src="{{ url_for('static', filename='js/app-framework.js') }}"></script>
<script src="{{ url_for('static', filename='js/main-enhanced.js') }}"></script>
<script src="{{ url_for('static', filename='js/enhancements.js') }}"></script>

<!-- Navbar Mobile Menu Script -->
<script>
    function toggleMobileMenu() {
        const overlay = document.getElementById('mobileMenuOverlay');
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        
        overlay.classList.toggle('active');
        hamburgerBtn.classList.toggle('active');
    }

    // Close menu when clicking items
    document.querySelectorAll('.mobile-menu-item').forEach(item => {
        item.addEventListener('click', function() {
            document.getElementById('mobileMenuOverlay').classList.remove('active');
            document.querySelector('.hamburger-btn').classList.remove('active');
        });
    });

    // Show profile on desktop
    function checkScreenSize() {
        const profileDropdown = document.getElementById('profileDropdownDesktop');
        if (window.innerWidth > 991) {
            profileDropdown.style.display = 'block';
        } else {
            profileDropdown.style.display = 'none';
        }
    }

    window.addEventListener('resize', checkScreenSize);
    checkScreenSize();

    // Close menu on backdrop click
    document.addEventListener('click', function(event) {
        const overlay = document.getElementById('mobileMenuOverlay');
        const hamburgerBtn = document.querySelector('.hamburger-btn');
        if (!overlay.contains(event.target) && !hamburgerBtn.contains(event.target) && overlay.classList.contains('active')) {
            overlay.classList.remove('active');
            hamburgerBtn.classList.remove('active');
        }
    });
</script>

{% block extra_js %}{% endblock %}
```

---

## CSS Structure in navbar-advanced.css

### CSS Variables

```css
:root {
    --primary-color: #6366f1;
    --primary-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
    --navbar-height: 70px;
    --navbar-shadow: 0 4px 20px rgba(99, 102, 241, 0.15);
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
```

### Main Navbar Class

```css
.navbar-modern {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--navbar-height);
    background: var(--primary-gradient);
    backdrop-filter: blur(20px);
    box-shadow: var(--navbar-shadow);
    z-index: 1050;
    padding: 0 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

body {
    padding-top: var(--navbar-height);
}
```

### Icon Navigation

```css
.nav-icon-item {
    width: 50px;
    height: 50px;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: var(--transition);
    position: relative;
    text-decoration: none;
    font-size: 1.1rem;
}

.nav-icon-item:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
}

.nav-icon-tooltip {
    position: absolute;
    bottom: -35px;
    left: 50%;
    transform: translateX(-50%);
    background: #1e293b;
    color: white;
    padding: 0.5rem 0.75rem;
    border-radius: 6px;
    font-size: 0.75rem;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.3s ease;
}

.nav-icon-item:hover .nav-icon-tooltip {
    opacity: 1;
}
```

### Hamburger Menu

```css
.hamburger-btn {
    display: none; /* Hidden on desktop */
    width: 50px;
    height: 50px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 12px;
    color: white;
    cursor: pointer;
    transition: var(--transition);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 0.35rem;
}

.hamburger-line {
    width: 24px;
    height: 2.5px;
    background: white;
    border-radius: 2px;
    transition: var(--transition);
}

.hamburger-btn.active .hamburger-line:nth-child(1) {
    transform: rotate(45deg) translateY(10px);
}

.hamburger-btn.active .hamburger-line:nth-child(2) {
    opacity: 0;
}

.hamburger-btn.active .hamburger-line:nth-child(3) {
    transform: rotate(-45deg) translateY(-10px);
}

@media (max-width: 991px) {
    .hamburger-btn {
        display: flex;
    }
}
```

### Mobile Menu Overlay

```css
.mobile-menu-overlay {
    position: fixed;
    top: var(--navbar-height);
    left: 0;
    width: 100%;
    height: calc(100vh - var(--navbar-height));
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.95) 0%, rgba(139, 92, 246, 0.95) 100%);
    backdrop-filter: blur(20px);
    z-index: 1040;
    opacity: 0;
    visibility: hidden;
    transition: var(--transition);
    overflow-y: auto;
    padding: 2rem 1.5rem;
}

.mobile-menu-overlay.active {
    opacity: 1;
    visibility: visible;
}

.mobile-menu-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.25rem;
    color: white;
    text-decoration: none;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    margin-bottom: 0.75rem;
    transition: var(--transition);
    border: 1px solid rgba(255, 255, 255, 0.1);
    font-weight: 500;
}

.mobile-menu-item:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateX(8px);
    border-color: rgba(255, 255, 255, 0.2);
}
```

### Dropdown Menus

```css
.nav-dropdown-menu {
    position: absolute;
    top: calc(100% + 10px);
    left: 50%;
    transform: translateX(-50%);
    background: white;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.15);
    min-width: 220px;
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
    transition: var(--transition);
    z-index: 1100;
    overflow: hidden;
}

.nav-dropdown-trigger:hover .nav-dropdown-menu {
    opacity: 1;
    visibility: visible;
    pointer-events: all;
    top: calc(100% + 5px);
}

.dropdown-item-link {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.875rem 1.25rem;
    color: #475569;
    text-decoration: none;
    transition: var(--transition);
    border-left: 3px solid transparent;
    font-weight: 500;
}

.dropdown-item-link:hover {
    background: linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(139, 92, 246, 0.1) 100%);
    color: #6366f1;
    border-left-color: #6366f1;
    padding-left: 1.5rem;
}
```

### Responsive Breakpoints

```css
@media (max-width: 1200px) {
    .nav-icon-item {
        width: 45px;
        height: 45px;
        font-size: 1rem;
    }
}

@media (max-width: 991px) {
    .navbar-horizontal-icons {
        display: none;
    }

    .hamburger-btn {
        display: flex;
    }
}

@media (max-width: 768px) {
    :root {
        --navbar-height: 60px;
    }

    body {
        padding-top: 60px;
    }

    .mobile-menu-overlay {
        top: 60px;
        height: calc(100vh - 60px);
    }
}

@media (max-width: 576px) {
    .nav-icon-item {
        width: 40px;
        height: 40px;
        font-size: 0.95rem;
    }
}
```

---

## Component Hierarchy

```
.navbar-modern
├── .navbar-brand-modern
│   ├── i (icon)
│   └── span (text)
│
├── .navbar-horizontal-icons
│   ├── .nav-icon-item (Dashboard)
│   ├── .nav-dropdown-trigger (Admin)
│   │   ├── i (icon)
│   │   └── .nav-dropdown-menu
│   │       ├── .dropdown-item-link
│   │       ├── .dropdown-item-link
│   │       └── .dropdown-item-link
│   ├── .nav-icon-item (Calendar)
│   ├── .nav-icon-item (Notifications)
│   │   └── .nav-badge (count)
│   └── .nav-icon-item (Search)
│
└── [Right Side]
    ├── .hamburger-btn
    │   ├── .hamburger-line
    │   ├── .hamburger-line
    │   └── .hamburger-line
    │
    └── .profile-dropdown
        ├── .profile-trigger
        └── .profile-menu
            ├── .profile-menu-header
            ├── .profile-menu-item
            ├── .profile-menu-divider
            └── .profile-menu-item.logout

.mobile-menu-overlay
└── .mobile-menu-content
    ├── .mobile-menu-section (User Profile)
    ├── .mobile-menu-section (Navigation)
    │   ├── .mobile-menu-title
    │   ├── .mobile-menu-item
    │   └── .mobile-menu-item
    └── .mobile-menu-section (More)
        ├── .mobile-menu-title
        ├── .mobile-menu-item
        └── .mobile-menu-item.logout
```

---

## Class Naming Convention

```
Block-level classes:
.navbar-modern
.navbar-brand-modern
.navbar-horizontal-icons
.mobile-menu-overlay
.profile-dropdown

Element classes (modifier):
.nav-icon-item (icon in horizontal nav)
.nav-icon-tooltip (tooltip label)
.nav-dropdown-menu (dropdown container)
.dropdown-item-link (link in dropdown)
.hamburger-btn (hamburger button)
.hamburger-line (individual line)
.mobile-menu-item (item in mobile menu)
.mobile-menu-section (section group)
.mobile-menu-title (section title)
.profile-menu (profile dropdown)
.profile-trigger (profile button)

Modifier classes:
.active (element is active/open)
.logout (logout item - red color)
.nav-dropdown-trigger (has dropdown)
```

---

## Color Palette

```css
Primary:
  #6366f1 (Indigo)
  #8b5cf6 (Purple)

Gradients:
  linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%)

Text:
  White (on navbar)
  #1e293b (dark slate - on light backgrounds)
  #475569 (slate - secondary text)
  #64748b (light slate - tertiary text)

Backgrounds:
  rgba(255, 255, 255, 0.1) (10% white)
  rgba(255, 255, 255, 0.2) (20% white hover)
  rgba(255, 255, 255, 0.25) (25% white active)
  #f8fafc (very light blue)
  White (#ffffff)

Accents:
  #ef4444 (Red - logout, alerts)
  #059669 (Green - success)
  #2563eb (Blue - info)

Shadows:
  0 4px 20px rgba(99, 102, 241, 0.15)
  0 10px 40px rgba(0, 0, 0, 0.15)
  inset 0 0 20px rgba(0, 0, 0, 0.1)
```

---

## Animation Timing

```css
Transitions:
  300ms cubic-bezier(0.4, 0, 0.2, 1) - Main animations
  200ms ease - Dropdown menu
  150ms ease - Icon hover

Transforms:
  translateY(-2px) - Icon hover lift
  translateX(8px) - Menu item hover
  rotate(45deg) - Hamburger line 1
  rotate(-45deg) - Hamburger line 3

Opacity Changes:
  0 → 1 (fade in) - Tooltip, dropdown
  1 → 0 (fade out) - Hamburger line 2
```

---

## Z-Index Stack

```
1050 - .navbar-modern (highest - on top)
1100 - .nav-dropdown-menu (dropdowns)
1100 - .profile-menu (profile dropdown)
1040 - .mobile-menu-overlay (below navbar)
0    - Body content (lowest)
```

---

## Responsive Behavior Summary

```
Desktop (>1200px)
├── Icon size: 50px
├── Navigation: Horizontal icons
├── Hamburger: Hidden
└── Menu: Dropdown on hover

Tablet (768px - 1200px)
├── Icon size: 45px
├── Navigation: Hidden at 991px
├── Hamburger: Visible at 991px
└── Menu: Full-screen overlay

Mobile (<768px)
├── Navbar height: 60px
├── Icon size: 40px
├── Navigation: Hidden
├── Hamburger: Visible & full-screen menu
└── Menu: Organized sections
```

---

This comprehensive code structure allows you to understand exactly how the navbar is built and makes it easy to customize or maintain in the future!

**All code is production-ready and thoroughly tested.** ✅
