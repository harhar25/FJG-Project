/**
 * IT Laboratory Schedule System - Enterprise JavaScript Framework
 * Version: 1.0.0
 * 
 * Features:
 * - Modular architecture with namespaced modules
 * - Error handling and logging
 * - Performance monitoring
 * - State management patterns
 * - Accessibility helpers
 * - Form validation
 * - API communication
 * - UI component management
 */

// ============================================================================
// GLOBAL APP NAMESPACE
// ============================================================================

window.App = window.App || {};

// ============================================================================
// CONFIGURATION
// ============================================================================

App.Config = {
    DEBUG: true,
    API_TIMEOUT: 5000,
    NOTIFICATION_DURATION: 5000,
    DEBOUNCE_DELAY: 300,
    LOG_LEVEL: 'info', // 'debug', 'info', 'warn', 'error'
};

// ============================================================================
// LOGGER MODULE
// ============================================================================

App.Logger = (function() {
    const levels = { debug: 0, info: 1, warn: 2, error: 3 };
    const currentLevel = levels[App.Config.LOG_LEVEL] || levels.info;
    
    const formatTime = () => new Date().toISOString();
    
    const shouldLog = (level) => levels[level] >= currentLevel;
    
    return {
        debug: function(message, data) {
            if (shouldLog('debug')) {
                console.log(`[${formatTime()}] DEBUG:`, message, data || '');
            }
        },
        
        info: function(message, data) {
            if (shouldLog('info')) {
                console.log(`[${formatTime()}] INFO:`, message, data || '');
            }
        },
        
        warn: function(message, data) {
            if (shouldLog('warn')) {
                console.warn(`[${formatTime()}] WARN:`, message, data || '');
            }
        },
        
        error: function(message, error) {
            if (shouldLog('error')) {
                console.error(`[${formatTime()}] ERROR:`, message, error || '');
            }
        },
        
        group: function(label) {
            console.group(`[${formatTime()}] ${label}`);
        },
        
        groupEnd: function() {
            console.groupEnd();
        }
    };
})();

// ============================================================================
// UTILITY MODULE
// ============================================================================

App.Util = {
    /**
     * Debounce a function call
     */
    debounce: function(func, wait, immediate) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                if (!immediate) func.apply(this, args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(this, args);
        };
    },
    
    /**
     * Throttle a function call
     */
    throttle: function(func, wait) {
        let timeout = null;
        let previous = 0;
        return function(...args) {
            const now = Date.now();
            if (now - previous > wait) {
                func.apply(this, args);
                previous = now;
            } else {
                clearTimeout(timeout);
                timeout = setTimeout(() => {
                    func.apply(this, args);
                    previous = Date.now();
                }, wait);
            }
        };
    },
    
    /**
     * Get DOM element with error handling
     */
    getElement: function(selector) {
        try {
            const element = document.querySelector(selector);
            if (!element) {
                App.Logger.warn(`Element not found: ${selector}`);
                return null;
            }
            return element;
        } catch (error) {
            App.Logger.error(`Invalid selector: ${selector}`, error);
            return null;
        }
    },
    
    /**
     * Get all DOM elements with error handling
     */
    getElements: function(selector) {
        try {
            return document.querySelectorAll(selector);
        } catch (error) {
            App.Logger.error(`Invalid selector: ${selector}`, error);
            return [];
        }
    },
    
    /**
     * Add event listener with cleanup support
     */
    addEventListener: function(element, event, handler) {
        if (!element) return;
        element.addEventListener(event, handler);
        return () => element.removeEventListener(event, handler);
    },
    
    /**
     * Format date to readable format
     */
    formatDate: function(date, format = 'MMM DD, YYYY') {
        if (!(date instanceof Date)) {
            date = new Date(date);
        }
        const options = {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        };
        return date.toLocaleDateString('en-US', options);
    },
    
    /**
     * Format time to HH:MM format
     */
    formatTime: function(date) {
        if (typeof date === 'string') {
            const [hours, minutes] = date.split(':');
            return `${hours}:${minutes}`;
        }
        if (date instanceof Date) {
            return date.toLocaleTimeString('en-US', {
                hour: '2-digit',
                minute: '2-digit',
                hour12: false
            });
        }
        return date;
    },
    
    /**
     * Safe JSON parse
     */
    parseJSON: function(json, fallback = null) {
        try {
            return JSON.parse(json);
        } catch (error) {
            App.Logger.warn('JSON parse error', error);
            return fallback;
        }
    },
    
    /**
     * Clone object
     */
    clone: function(obj) {
        return JSON.parse(JSON.stringify(obj));
    }
};

// ============================================================================
// API MODULE
// ============================================================================

App.API = (function() {
    const request = async (method, url, data = null, options = {}) => {
        const config = {
            method,
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
                ...options.headers
            },
            timeout: App.Config.API_TIMEOUT,
            ...options
        };
        
        if (data) {
            config.body = JSON.stringify(data);
        }
        
        try {
            const response = await fetch(url, config);
            
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}: ${response.statusText}`);
            }
            
            const contentType = response.headers.get('content-type');
            if (contentType && contentType.includes('application/json')) {
                return await response.json();
            }
            return await response.text();
        } catch (error) {
            App.Logger.error(`API request failed: ${method} ${url}`, error);
            throw error;
        }
    };
    
    return {
        get: (url, options) => request('GET', url, null, options),
        post: (url, data, options) => request('POST', url, data, options),
        put: (url, data, options) => request('PUT', url, data, options),
        delete: (url, options) => request('DELETE', url, null, options),
        patch: (url, data, options) => request('PATCH', url, data, options)
    };
})();

// ============================================================================
// UI MODULE - NOTIFICATIONS & TOASTS
// ============================================================================

App.UI = (function() {
    const showNotification = (message, type = 'info', duration = App.Config.NOTIFICATION_DURATION) => {
        const alertClass = `alert-${type}`;
        const icon = {
            success: 'fa-check-circle',
            danger: 'fa-exclamation-circle',
            warning: 'fa-exclamation-triangle',
            info: 'fa-info-circle'
        }[type] || 'fa-info-circle';
        
        const alert = document.createElement('div');
        alert.className = `alert ${alertClass} alert-dismissible fade show`;
        alert.setAttribute('role', 'alert');
        alert.innerHTML = `
            <i class="fas ${icon}"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        
        const container = document.querySelector('[role="main"]') || document.body;
        container.insertBefore(alert, container.firstChild);
        
        if (duration > 0) {
            setTimeout(() => {
                alert.remove();
            }, duration);
        }
        
        return alert;
    };
    
    const showToast = (title, message, type = 'info') => {
        const toast = App.Util.getElement('#liveToast');
        if (!toast) return;
        
        document.getElementById('toast-title').textContent = title;
        document.getElementById('toast-message').textContent = message;
        
        toast.classList.remove('bg-primary', 'bg-success', 'bg-danger', 'bg-warning');
        toast.classList.add(`bg-${type}`);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
    };
    
    const showLoader = (element, show = true) => {
        if (!element) return;
        if (show) {
            element.classList.add('opacity-50');
            element.setAttribute('aria-busy', 'true');
            const spinner = document.createElement('div');
            spinner.className = 'spinner-border spinner-border-sm ms-2';
            spinner.setAttribute('role', 'status');
            element.appendChild(spinner);
        } else {
            element.classList.remove('opacity-50');
            element.setAttribute('aria-busy', 'false');
            const spinner = element.querySelector('.spinner-border');
            if (spinner) spinner.remove();
        }
    };
    
    return {
        showNotification,
        showToast,
        showLoader,
        
        showError: (message) => showNotification(message, 'danger'),
        showSuccess: (message) => showNotification(message, 'success'),
        showWarning: (message) => showNotification(message, 'warning'),
        showInfo: (message) => showNotification(message, 'info')
    };
})();

// ============================================================================
// FORM VALIDATION MODULE
// ============================================================================

App.Form = (function() {
    const validators = {
        required: (value) => value && value.trim().length > 0,
        email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
        phone: (value) => /^[\d\s\-\(\)]+$/.test(value),
        number: (value) => !isNaN(value) && value !== '',
        min: (value, min) => value.length >= min,
        max: (value, max) => value.length <= max,
        match: (value, selector) => value === document.querySelector(selector)?.value
    };
    
    const validateForm = (formSelector) => {
        const form = App.Util.getElement(formSelector);
        if (!form) return false;
        
        const inputs = form.querySelectorAll('[data-validate]');
        let isValid = true;
        
        inputs.forEach(input => {
            const rules = input.dataset.validate.split('|');
            let inputValid = true;
            
            for (const rule of rules) {
                const [validatorName, ...args] = rule.split(':');
                const validator = validators[validatorName];
                
                if (validator && !validator(input.value, ...args)) {
                    inputValid = false;
                    break;
                }
            }
            
            if (!inputValid) {
                input.classList.add('is-invalid');
                isValid = false;
            } else {
                input.classList.remove('is-invalid');
            }
        });
        
        return isValid;
    };
    
    return {
        validateForm,
        validators
    };
})();

// ============================================================================
// STATE MANAGEMENT MODULE
// ============================================================================

App.State = (function() {
    const state = {};
    const listeners = new Map();
    
    const subscribe = (key, callback) => {
        if (!listeners.has(key)) {
            listeners.set(key, []);
        }
        listeners.get(key).push(callback);
        
        // Return unsubscribe function
        return () => {
            const callbacks = listeners.get(key);
            const index = callbacks.indexOf(callback);
            if (index > -1) callbacks.splice(index, 1);
        };
    };
    
    const notify = (key) => {
        if (listeners.has(key)) {
            listeners.get(key).forEach(callback => callback(state[key]));
        }
    };
    
    return {
        get: (key) => state[key],
        set: (key, value) => {
            if (state[key] !== value) {
                state[key] = value;
                notify(key);
            }
        },
        update: (key, updater) => {
            const newValue = updater(state[key]);
            this.set(key, newValue);
        },
        subscribe,
        getState: () => App.Util.clone(state)
    };
})();

// ============================================================================
// PERFORMANCE MONITORING MODULE
// ============================================================================

App.Monitor = (function() {
    const metrics = {
        pageLoadTime: 0,
        apiCalls: [],
        errors: []
    };
    
    const recordMetric = (name, value, unit = 'ms') => {
        App.Logger.debug(`Metric: ${name} = ${value}${unit}`);
    };
    
    const recordApiCall = (url, duration, status) => {
        metrics.apiCalls.push({ url, duration, status, timestamp: Date.now() });
    };
    
    const recordError = (message, stack) => {
        metrics.errors.push({ message, stack, timestamp: Date.now() });
    };
    
    const getMetrics = () => metrics;
    
    return {
        recordMetric,
        recordApiCall,
        recordError,
        getMetrics
    };
})();

// ============================================================================
// ACCESSIBILITY MODULE
// ============================================================================

App.Accessibility = {
    /**
     * Announce message to screen readers
     */
    announce: function(message, priority = 'polite') {
        const announcement = document.createElement('div');
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', priority);
        announcement.className = 'sr-only';
        announcement.textContent = message;
        document.body.appendChild(announcement);
        
        setTimeout(() => announcement.remove(), 1000);
    },
    
    /**
     * Focus element and announce
     */
    focusElement: function(selector, message) {
        const element = App.Util.getElement(selector);
        if (element) {
            element.focus();
            if (message) {
                this.announce(message, 'assertive');
            }
        }
    },
    
    /**
     * Check keyboard navigation support
     */
    isKeyboardUser: function() {
        return !navigator.userAgentData?.platform || 
               navigator.userAgentData.platform !== 'mobile';
    }
};

// ============================================================================
// MAIN APP MONITOR (Page Lifecycle)
// ============================================================================

App.Monitor = {
    init: function() {
        App.Logger.info('Initializing application...');
        
        // Track page visibility
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                App.Logger.debug('Page hidden');
            } else {
                App.Logger.debug('Page visible');
            }
        });
        
        // Track errors globally
        window.addEventListener('error', (event) => {
            App.Logger.error('Uncaught error', event.error);
            App.Monitor.recordError(event.message, event.error?.stack);
        });
        
        // Track unhandled promise rejections
        window.addEventListener('unhandledrejection', (event) => {
            App.Logger.error('Unhandled promise rejection', event.reason);
            App.Monitor.recordError(event.reason?.message, event.reason?.stack);
        });
        
        App.Logger.info('Application initialized successfully');
    },
    
    recordError: function(message, stack) {
        App.Monitor.recordError(message, stack);
    }
};

// ============================================================================
// NOTIFICATION COUNTER MODULE
// ============================================================================

App.Notifications = {
    updateCount: function() {
        const updateBadge = App.Util.debounce(async () => {
            try {
                const response = await App.API.get('/api/notifications/unread');
                const badge = App.Util.getElement('#notif-badge');
                if (badge) {
                    const count = response.count || 0;
                    if (count > 0) {
                        badge.textContent = count;
                        badge.classList.remove('d-none');
                    } else {
                        badge.classList.add('d-none');
                    }
                }
            } catch (error) {
                App.Logger.warn('Failed to update notification count', error);
            }
        }, App.Config.DEBOUNCE_DELAY);
        
        updateBadge();
        
        // Update every 30 seconds
        setInterval(updateBadge, 30000);
    }
};

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    App.Logger.info('DOM Content Loaded');
    
    // Initialize modules
    App.Monitor.init();
    App.Notifications.updateCount();
    
    // Global error handler for forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            if (this.getAttribute('data-validate') === 'true') {
                if (!App.Form.validateForm(`#${this.id}`)) {
                    e.preventDefault();
                    App.UI.showError('Please fix the form errors');
                }
            }
        });
    });
});

// ============================================================================
// EXPORT FOR EXTERNAL USE
// ============================================================================

if (typeof module !== 'undefined' && module.exports) {
    module.exports = App;
}
