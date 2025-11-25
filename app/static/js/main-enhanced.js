/**
 * IT Laboratory Schedule System - Main Application Script
 * Version: 1.0.0
 * 
 * Integrates with App Framework for enterprise-grade functionality
 * Features: Error handling, performance monitoring, accessibility, state management
 */

// ============================================================================
// INITIALIZATION
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    App.Logger.info('Initializing main application script');
    
    // Initialize date inputs
    initializeDateInputs();
    
    // Initialize tooltips and popovers
    initializeBootstrapComponents();
    
    // Setup form validation
    setupFormValidation();
    
    // Setup event listeners
    setupEventListeners();
    
    App.Logger.info('Main application script initialized');
});

// ============================================================================
// UTILITY FUNCTIONS - ENHANCED
// ============================================================================

/**
 * Format time to 12-hour format
 * @param {string} time - Time in HH:MM format
 * @returns {string} Formatted time
 */
function formatTime(time) {
    try {
        const [hours, minutes] = time.split(':');
        const hour = parseInt(hours);
        const ampm = hour >= 12 ? 'PM' : 'AM';
        const displayHour = hour % 12 || 12;
        return `${displayHour}:${minutes} ${ampm}`;
    } catch (error) {
        App.Logger.warn('Error formatting time', error);
        return time;
    }
}

/**
 * Format date to readable format
 * @param {Date|string} date - Date object or string
 * @returns {string} Formatted date
 */
function formatDate(date) {
    return App.Util.formatDate(date);
}

/**
 * Calculate duration between two times
 * @param {string} startTime - Start time in HH:MM format
 * @param {string} endTime - End time in HH:MM format
 * @returns {string} Duration in "Xh Xm" format
 */
function calculateDuration(startTime, endTime) {
    try {
        const start = new Date(`2000-01-01 ${startTime}`);
        const end = new Date(`2000-01-01 ${endTime}`);
        const diff = end - start;
        const hours = Math.floor(diff / 3600000);
        const minutes = Math.floor((diff % 3600000) / 60000);
        return `${hours}h ${minutes}m`;
    } catch (error) {
        App.Logger.warn('Error calculating duration', error);
        return 'Invalid times';
    }
}

/**
 * Parse URL query parameters
 * @param {string} name - Parameter name
 * @returns {string} Parameter value
 */
function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

/**
 * Debounce function
 * @param {Function} func - Function to debounce
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} Debounced function
 */
function debounce(func, wait) {
    return App.Util.debounce(func, wait);
}

/**
 * Throttle function
 * @param {Function} func - Function to throttle
 * @param {number} wait - Wait time in milliseconds
 * @returns {Function} Throttled function
 */
function throttle(func, wait) {
    return App.Util.throttle(func, wait);
}

/**
 * Format bytes to human-readable format
 * @param {number} bytes - Number of bytes
 * @param {number} decimals - Number of decimals
 * @returns {string} Formatted bytes
 */
function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

// ============================================================================
// NOTIFICATION FUNCTIONS
// ============================================================================

/**
 * Show success notification
 * @param {string} message - Message to display
 */
function showSuccess(message) {
    App.UI.showSuccess(message);
}

/**
 * Show error notification
 * @param {string} message - Message to display
 */
function showError(message) {
    App.UI.showError(message);
}

/**
 * Show warning notification
 * @param {string} message - Message to display
 */
function showWarning(message) {
    App.UI.showWarning(message);
}

/**
 * Show info notification
 * @param {string} message - Message to display
 */
function showInfo(message) {
    App.UI.showInfo(message);
}

/**
 * Show loading state on element
 * @param {string|Element} element - Element selector or element
 */
function showLoader(element) {
    const el = typeof element === 'string' ? App.Util.getElement(element) : element;
    App.UI.showLoader(el, true);
}

/**
 * Hide loading state on element
 * @param {string|Element} element - Element selector or element
 */
function hideLoader(element) {
    const el = typeof element === 'string' ? App.Util.getElement(element) : element;
    App.UI.showLoader(el, false);
}

/**
 * Mark notification as read
 * @param {number} notificationId - Notification ID
 */
function markNotificationAsRead(notificationId) {
    const url = `/api/notifications/mark-read/${notificationId}`;
    
    App.API.post(url, {})
        .then(data => {
            if (data.success) {
                App.Notifications.updateCount();
            }
        })
        .catch(error => {
            App.Logger.error('Error marking notification as read', error);
        });
}

/**
 * Update notification count
 */
function updateNotificationCount() {
    App.Notifications.updateCount();
}

// ============================================================================
// TABLE FUNCTIONS
// ============================================================================

/**
 * Search/filter table content
 * @param {string} inputId - Search input ID
 * @param {string} tableId - Table ID
 */
function searchTable(inputId, tableId) {
    const input = App.Util.getElement(`#${inputId}`);
    const table = App.Util.getElement(`#${tableId}`);
    
    if (!input || !table) {
        App.Logger.warn(`Search table: input or table not found`);
        return;
    }
    
    const debouncedSearch = debounce(() => {
        const filter = input.value.toUpperCase();
        const rows = table.querySelectorAll('tbody tr');
        let visibleCount = 0;
        
        rows.forEach(row => {
            const text = row.textContent || row.innerText;
            const isMatch = text.toUpperCase().includes(filter);
            row.style.display = isMatch ? '' : 'none';
            if (isMatch) visibleCount++;
        });
        
        App.Logger.debug(`Search results: ${visibleCount} rows visible`);
    }, App.Config.DEBOUNCE_DELAY);
    
    input.addEventListener('keyup', debouncedSearch);
}

/**
 * Export table to CSV
 * @param {string} tableId - Table ID
 * @param {string} filename - Output filename
 */
function exportTableToCSV(tableId, filename = 'export.csv') {
    try {
        const table = App.Util.getElement(`#${tableId}`);
        if (!table) {
            App.UI.showError('Table not found');
            return;
        }
        
        const csv = [];
        const rows = table.querySelectorAll('tr');
        
        rows.forEach(row => {
            const cols = row.querySelectorAll('td, th');
            const csvRow = [];
            cols.forEach(col => {
                csvRow.push('"' + col.innerText.trim() + '"');
            });
            csv.push(csvRow.join(','));
        });
        
        downloadFile(csv.join('\n'), filename, 'text/csv');
        App.UI.showSuccess('Table exported successfully');
    } catch (error) {
        App.Logger.error('Error exporting table to CSV', error);
        App.UI.showError('Error exporting table');
    }
}

/**
 * Print page element
 * @param {string} elementId - Element ID to print
 */
function printContent(elementId) {
    try {
        const element = App.Util.getElement(`#${elementId}`);
        if (!element) {
            App.UI.showError('Element not found for printing');
            return;
        }
        
        const printWindow = window.open('', '', 'height=800,width=1000');
        if (!printWindow) {
            App.UI.showError('Unable to open print window');
            return;
        }
        
        printWindow.document.write('<html><head><title>Print</title>');
        printWindow.document.write('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">');
        printWindow.document.write('<style>@media print { body { margin: 0; padding: 10px; } }</style>');
        printWindow.document.write('</head><body>');
        printWindow.document.write(element.innerHTML);
        printWindow.document.write('</body></html>');
        printWindow.document.close();
        printWindow.focus();
        
        setTimeout(() => {
            printWindow.print();
        }, 250);
    } catch (error) {
        App.Logger.error('Error printing content', error);
        App.UI.showError('Error printing content');
    }
}

/**
 * Download file
 * @param {string} content - File content
 * @param {string} filename - Filename
 * @param {string} type - MIME type
 */
function downloadFile(content, filename, type = 'text/plain') {
    try {
        const file = new Blob([content], { type });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(file);
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(link.href);
    } catch (error) {
        App.Logger.error('Error downloading file', error);
        App.UI.showError('Error downloading file');
    }
}

// ============================================================================
// FORM FUNCTIONS
// ============================================================================

/**
 * Validate form
 * @param {string} formId - Form ID
 * @returns {boolean} Is form valid
 */
function validateForm(formId) {
    return App.Form.validateForm(`#${formId}`);
}

/**
 * Reset form
 * @param {string} formId - Form ID
 */
function resetForm(formId) {
    const form = App.Util.getElement(`#${formId}`);
    if (form) {
        form.reset();
    }
}

/**
 * Disable form submit button
 * @param {string} formId - Form ID
 */
function disableFormSubmit(formId) {
    const form = App.Util.getElement(`#${formId}`);
    if (form) {
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            showLoader(submitBtn);
        }
    }
}

/**
 * Enable form submit button
 * @param {string} formId - Form ID
 */
function enableFormSubmit(formId) {
    const form = App.Util.getElement(`#${formId}`);
    if (form) {
        const submitBtn = form.querySelector('button[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = false;
            hideLoader(submitBtn);
        }
    }
}

// ============================================================================
// SCHEDULE/TIME FUNCTIONS
// ============================================================================

/**
 * Get schedule time blocks via AJAX
 * @param {number} labId - Lab ID
 * @param {string} date - Date in YYYY-MM-DD format
 */
function getTimeBlocks(labId, date) {
    if (!labId || !date) {
        App.Logger.warn('Lab ID and date are required');
        return;
    }
    
    const url = `/api/schedule/time-blocks?lab_id=${labId}&date=${date}`;
    
    App.API.get(url)
        .then(data => {
            displayTimeBlocks(data.time_blocks || []);
        })
        .catch(error => {
            App.Logger.error('Error fetching time blocks', error);
            displayTimeBlocks([]);
        });
}

/**
 * Display time blocks
 * @param {Array} blocks - Array of time blocks
 */
function displayTimeBlocks(blocks) {
    const container = App.Util.getElement('#timeBlocksContainer');
    if (!container) return;
    
    if (!blocks || blocks.length === 0) {
        container.innerHTML = '<p class="text-muted text-center py-4">No schedules available for this selection</p>';
        return;
    }
    
    let html = '<div class="list-group">';
    
    blocks.forEach(block => {
        const statusColor = {
            'Available': 'success',
            'Reserved': 'info',
            'Maintenance': 'danger',
            'Conflict': 'warning'
        }[block.status] || 'secondary';
        
        const statusIcon = {
            'Available': 'fa-check-circle',
            'Reserved': 'fa-calendar-check',
            'Maintenance': 'fa-tools',
            'Conflict': 'fa-exclamation-circle'
        }[block.status] || 'fa-circle';
        
        html += `
            <div class="list-group-item list-group-item-action" role="button" tabindex="0">
                <div class="d-flex justify-content-between align-items-start">
                    <div class="flex-grow-1">
                        <div class="fw-semibold">
                            <i class="fas fa-clock me-2"></i>
                            ${block.start_time} - ${block.end_time}
                        </div>
                        <small class="text-muted d-block mt-1">
                            <i class="fas fa-book me-1"></i>
                            ${block.course || 'N/A'} - ${block.section || 'N/A'}
                        </small>
                    </div>
                    <span class="badge bg-${statusColor}">
                        <i class="fas ${statusIcon} me-1"></i>
                        ${block.status}
                    </span>
                </div>
            </div>
        `;
    });
    
    html += '</div>';
    container.innerHTML = html;
}

// ============================================================================
// INITIALIZATION FUNCTIONS
// ============================================================================

/**
 * Initialize date inputs with minimum date constraint
 */
function initializeDateInputs() {
    const today = new Date().toISOString().split('T')[0];
    const dateInputs = document.querySelectorAll('input[type="date"]');
    
    dateInputs.forEach(input => {
        if (input.name === 'requested_date' || input.name === 'date_from' || input.name === 'date_to') {
            input.min = today;
            input.addEventListener('change', function() {
                const selectedDate = new Date(this.value);
                const today = new Date();
                today.setHours(0, 0, 0, 0);
                
                if (selectedDate < today) {
                    showError('Please select a future date');
                    this.value = '';
                }
            });
        }
    });
}

/**
 * Initialize Bootstrap components (tooltips, popovers, etc.)
 */
function initializeBootstrapComponents() {
    // Initialize tooltips
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipElements.forEach(element => {
        new bootstrap.Tooltip(element);
    });
    
    // Initialize popovers
    const popoverElements = document.querySelectorAll('[data-bs-toggle="popover"]');
    popoverElements.forEach(element => {
        new bootstrap.Popover(element);
    });
}

/**
 * Setup form validation
 */
function setupFormValidation() {
    const forms = document.querySelectorAll('form[data-validate="true"]');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!validateForm(this.id)) {
                e.preventDefault();
                e.stopPropagation();
                showError('Please fix the form errors');
            }
            this.classList.add('was-validated');
        });
    });
}

/**
 * Setup event listeners for common interactions
 */
function setupEventListeners() {
    // Confirm dialogs
    document.querySelectorAll('[data-confirm]').forEach(element => {
        element.addEventListener('click', function(e) {
            const message = this.dataset.confirm || 'Are you sure?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });
    
    // Auto-dismiss alerts after 5 seconds
    document.querySelectorAll('.alert:not(.alert-persistent)').forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, App.Config.NOTIFICATION_DURATION);
    });
    
    // Keyboard navigation for cards
    document.querySelectorAll('.list-group-item[role="button"]').forEach(item => {
        item.addEventListener('keypress', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                this.click();
            }
        });
    });
}

// ============================================================================
// WINDOW ERROR HANDLERS
// ============================================================================

window.addEventListener('error', function(event) {
    App.Logger.error('Uncaught error', event.error);
});

window.addEventListener('unhandledrejection', function(event) {
    App.Logger.error('Unhandled promise rejection', event.reason);
});

// ============================================================================
// PERFORMANCE MONITORING
// ============================================================================

if (window.performance && window.performance.timing) {
    window.addEventListener('load', function() {
        setTimeout(function() {
            const perfData = window.performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            App.Monitor.recordMetric('Page Load Time', pageLoadTime);
            App.Logger.info(`Page loaded in ${pageLoadTime}ms`);
        }, 0);
    });
}

// ============================================================================
// EXPORT FUNCTIONS FOR GLOBAL USE
// ============================================================================

// Make key functions globally accessible for backward compatibility
window.updateNotificationCount = updateNotificationCount;
window.formatTime = formatTime;
window.formatDate = formatDate;
window.calculateDuration = calculateDuration;
window.getUrlParameter = getUrlParameter;
window.debounce = debounce;
window.throttle = throttle;
window.showSuccess = showSuccess;
window.showError = showError;
window.showWarning = showWarning;
window.showInfo = showInfo;
window.searchTable = searchTable;
window.exportTableToCSV = exportTableToCSV;
window.printContent = printContent;
window.validateForm = validateForm;
