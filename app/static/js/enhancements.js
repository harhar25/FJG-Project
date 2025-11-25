/**
 * ENHANCED APPLICATION INTERACTIVITY
 * Provides modern features for all pages
 */

// ============================================
// TABLE ENHANCEMENTS
// ============================================

class TableEnhancer {
    constructor() {
        this.init();
    }

    init() {
        this.addTableSort();
        this.addTableSearch();
        this.addRowAnimations();
    }

    addTableSort() {
        const tables = document.querySelectorAll('.table thead th');
        tables.forEach((th, index) => {
            th.style.cursor = 'pointer';
            th.setAttribute('data-column', index);
            
            th.addEventListener('click', (e) => {
                if (e.target.closest('i')) return;
                const icon = th.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-arrow-up');
                    icon.classList.toggle('fa-arrow-down');
                }
            });
        });
    }

    addTableSearch() {
        const tables = document.querySelectorAll('.table');
        tables.forEach(table => {
            const searchInput = document.createElement('input');
            searchInput.type = 'text';
            searchInput.placeholder = 'Search table...';
            searchInput.className = 'form-control mb-3';
            searchInput.style.maxWidth = '300px';
            
            const tableWrapper = table.closest('.table-responsive') || table.parentElement;
            tableWrapper.parentElement.insertBefore(searchInput, tableWrapper);
            
            searchInput.addEventListener('keyup', (e) => {
                const filter = e.target.value.toLowerCase();
                const rows = table.querySelectorAll('tbody tr');
                
                rows.forEach(row => {
                    const text = row.textContent.toLowerCase();
                    row.style.display = text.includes(filter) ? '' : 'none';
                });
            });
        });
    }

    addRowAnimations() {
        const rows = document.querySelectorAll('.table tbody tr');
        rows.forEach((row, index) => {
            row.style.animation = `fadeIn 0.3s ease-out ${index * 0.05}s`;
        });
    }
}

// ============================================
// FORM VALIDATION & ENHANCEMENT
// ============================================

class FormEnhancer {
    constructor() {
        this.init();
    }

    init() {
        this.enhanceFormFields();
        this.addFormValidation();
        this.addPasswordStrength();
    }

    enhanceFormFields() {
        const inputs = document.querySelectorAll('.form-control, .form-select');
        inputs.forEach(input => {
            // Add floating label effect
            input.addEventListener('focus', () => {
                input.parentElement.classList.add('focused');
            });

            input.addEventListener('blur', () => {
                if (!input.value) {
                    input.parentElement.classList.remove('focused');
                }
            });

            // Add input icon animation
            if (input.previousElementSibling?.classList.contains('input-icon')) {
                input.addEventListener('focus', () => {
                    input.previousElementSibling.style.color = '#667eea';
                });

                input.addEventListener('blur', () => {
                    input.previousElementSibling.style.color = '#adb5bd';
                });
            }
        });
    }

    addFormValidation() {
        const forms = document.querySelectorAll('form');
        forms.forEach(form => {
            form.addEventListener('submit', (e) => {
                let isValid = true;

                const inputs = form.querySelectorAll('.form-control[required], .form-select[required]');
                inputs.forEach(input => {
                    if (!input.value.trim()) {
                        input.classList.add('is-invalid');
                        isValid = false;

                        // Show error message
                        let errorMsg = input.parentElement.querySelector('.invalid-feedback');
                        if (!errorMsg) {
                            errorMsg = document.createElement('div');
                            errorMsg.className = 'invalid-feedback d-block';
                            errorMsg.textContent = `${input.previousElementSibling?.textContent || 'This field'} is required`;
                            input.parentElement.appendChild(errorMsg);
                        }
                    } else {
                        input.classList.remove('is-invalid');
                        const errorMsg = input.parentElement.querySelector('.invalid-feedback');
                        if (errorMsg) errorMsg.remove();
                    }
                });

                if (!isValid) {
                    e.preventDefault();
                    this.showNotification('Please fill all required fields', 'danger');
                }
            });
        });
    }

    addPasswordStrength() {
        const passwordInputs = document.querySelectorAll('input[type="password"]');
        passwordInputs.forEach(input => {
            if (input.id && input.id.includes('password')) {
                input.addEventListener('input', () => {
                    const strength = this.calculatePasswordStrength(input.value);
                    this.updatePasswordIndicator(input, strength);
                });
            }
        });
    }

    calculatePasswordStrength(password) {
        let strength = 0;
        if (password.length >= 8) strength++;
        if (password.length >= 12) strength++;
        if (/[a-z]/.test(password) && /[A-Z]/.test(password)) strength++;
        if (/\d/.test(password)) strength++;
        if (/[!@#$%^&*]/.test(password)) strength++;
        return strength;
    }

    updatePasswordIndicator(input, strength) {
        let indicator = input.nextElementSibling;
        if (!indicator || !indicator.classList.contains('password-strength-indicator')) {
            indicator = document.createElement('div');
            indicator.className = 'password-strength-indicator mt-2';
            input.parentElement.appendChild(indicator);
        }

        const colors = ['#dc3545', '#ffc107', '#0d6efd', '#198754', '#20c997'];
        indicator.style.height = '4px';
        indicator.style.background = colors[Math.min(strength, 4)];
        indicator.style.borderRadius = '2px';
        indicator.style.transition = 'all 0.3s ease';
    }

    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `alert alert-${type} alert-dismissible fade show`;
        notification.innerHTML = `
            <i class="fas fa-info-circle me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        `;
        document.body.insertBefore(notification, document.body.firstChild);

        setTimeout(() => {
            notification.remove();
        }, 5000);
    }
}

// ============================================
// MODAL ENHANCEMENTS
// ============================================

class ModalEnhancer {
    constructor() {
        this.init();
    }

    init() {
        const modals = document.querySelectorAll('.modal');
        modals.forEach(modal => {
            modal.addEventListener('show.bs.modal', () => {
                modal.style.animation = 'slideDown 0.3s ease-out';
            });
        });
    }
}

// ============================================
// NOTIFICATION SYSTEM
// ============================================

class NotificationSystem {
    static init() {
        // Handle flash messages
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            if (!alert.querySelector('.alert-warning')) {
                setTimeout(() => {
                    const bsAlert = new bootstrap.Alert(alert);
                    bsAlert.close();
                }, 5000);
            }
        });

        // Add notification badge handler
        this.updateNotificationBadge();
    }

    static updateNotificationBadge() {
        const badge = document.getElementById('notif-badge');
        if (badge) {
            const count = parseInt(badge.textContent) || 0;
            if (count > 0) {
                badge.classList.remove('d-none');
            }
        }
    }

    static show(message, type = 'info', duration = 5000) {
        const toast = document.getElementById('liveToast');
        if (toast) {
            document.getElementById('toast-title').textContent = type.charAt(0).toUpperCase() + type.slice(1);
            document.getElementById('toast-message').textContent = message;
            
            const bsToast = new bootstrap.Toast(toast);
            bsToast.show();

            if (duration) {
                setTimeout(() => bsToast.hide(), duration);
            }
        }
    }
}

// ============================================
// PAGE ANIMATIONS
// ============================================

class PageAnimations {
    static init() {
        // Fade in elements on page load
        document.querySelectorAll('[data-animate]').forEach((el, index) => {
            const delay = index * 0.1;
            el.style.animation = `fadeIn 0.5s ease-out ${delay}s`;
            el.style.opacity = '0';
            el.style.animationFillMode = 'forwards';
        });

        // Scroll animations
        this.initScrollAnimations();
    }

    static initScrollAnimations() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                    entry.target.style.animation = 'slideDown 0.5s ease-out';
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.card, .table-responsive').forEach(el => {
            observer.observe(el);
        });
    }
}

// ============================================
// INITIALIZATION
// ============================================

document.addEventListener('DOMContentLoaded', () => {
    // Initialize all enhancers
    new TableEnhancer();
    new FormEnhancer();
    new ModalEnhancer();
    NotificationSystem.init();
    PageAnimations.init();

    // Add keyboard shortcuts
    document.addEventListener('keydown', (e) => {
        // Ctrl/Cmd + S to focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 's') {
            e.preventDefault();
            const searchInput = document.querySelector('[placeholder*="Search"]');
            if (searchInput) searchInput.focus();
        }
    });

    console.log('✨ Application enhanced with modern features');
});

// ============================================
// UTILITY FUNCTIONS
// ============================================

window.AppUtils = {
    formatDate: (date) => {
        return new Date(date).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });
    },

    formatTime: (time) => {
        return new Date(`2000-01-01 ${time}`).toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
        });
    },

    debounce: (func, wait) => {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    showConfirm: (message) => {
        return confirm(message);
    },

    copyToClipboard: (text) => {
        navigator.clipboard.writeText(text).then(() => {
            NotificationSystem.show('Copied to clipboard!', 'success');
        });
    }
};

// ============================================
// CUSTOM STYLES FOR FORM VALIDATION
// ============================================

const style = document.createElement('style');
style.textContent = `
    .form-control.is-invalid,
    .form-select.is-invalid {
        border-color: #dc3545 !important;
        background-color: rgba(220, 53, 69, 0.05) !important;
    }

    .form-control.is-invalid:focus,
    .form-select.is-invalid:focus {
        border-color: #dc3545 !important;
        box-shadow: 0 0 0 3px rgba(220, 53, 69, 0.1) !important;
    }

    .invalid-feedback {
        color: #dc3545;
        font-size: 0.85rem;
        font-weight: 500;
        margin-top: 0.5rem;
    }

    .password-strength-indicator {
        width: 100%;
        height: 4px;
        border-radius: 2px;
        background: #e0e0e0;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-10px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(style);
