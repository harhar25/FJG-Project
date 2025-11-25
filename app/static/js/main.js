/* Main JavaScript for Lab Schedule System */

document.addEventListener('DOMContentLoaded', function() {
    // Update unread notification count
    updateNotificationCount();
    
    // Refresh notification count every 30 seconds
    setInterval(updateNotificationCount, 30000);
    
    // Initialize tooltips
    initializeTooltips();
    
    // Set minimum date for date inputs
    setMinimumDate();
});

/**
 * Update unread notification count
 */
function updateNotificationCount() {
    fetch('/api/notifications/unread')
        .then(response => response.json())
        .then(data => {
            const badge = document.getElementById('notif-badge');
            if (badge) {
                if (data.unread_count > 0) {
                    badge.textContent = data.unread_count;
                    badge.classList.remove('d-none');
                } else {
                    badge.classList.add('d-none');
                }
            }
        })
        .catch(error => console.error('Error fetching notifications:', error));
}

/**
 * Initialize tooltips
 */
function initializeTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Set minimum date for date inputs
 */
function setMinimumDate() {
    const dateInputs = document.querySelectorAll('input[type="date"]');
    const today = new Date().toISOString().split('T')[0];
    
    dateInputs.forEach(input => {
        if (input.name === 'requested_date' || input.name === 'date_from' || input.name === 'date_to') {
            input.min = today;
        }
    });
}

/**
 * Confirm action before submission
 */
function confirmAction(message = 'Are you sure?') {
    return confirm(message);
}

/**
 * Format time to 12-hour format
 */
function formatTime(time) {
    const [hours, minutes] = time.split(':');
    const hour = parseInt(hours);
    const ampm = hour >= 12 ? 'PM' : 'AM';
    const displayHour = hour % 12 || 12;
    return `${displayHour}:${minutes} ${ampm}`;
}

/**
 * Format date to readable format
 */
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(date).toLocaleDateString('en-US', options);
}

/**
 * Show loading spinner
 */
function showLoading() {
    const spinnerHtml = `
        <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
    `;
    document.body.innerHTML += spinnerHtml;
}

/**
 * Hide loading spinner
 */
function hideLoading() {
    const spinner = document.querySelector('.spinner-border');
    if (spinner) {
        spinner.remove();
    }
}

/**
 * Show alert message
 */
function showAlert(message, type = 'success') {
    const alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    const container = document.querySelector('.container-fluid');
    if (container) {
        container.insertAdjacentHTML('afterbegin', alertHtml);
    }
}

/**
 * Validate form before submission
 */
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return true;
    
    return form.checkValidity() === false ? (event.preventDefault(), event.stopPropagation(), false) : true;
}

/**
 * Parse query parameters from URL
 */
function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    const regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    const results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
}

/**
 * Mark notification as read
 */
function markNotificationAsRead(notificationId) {
    fetch(`/api/notifications/mark-read/${notificationId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateNotificationCount();
        }
    })
    .catch(error => console.error('Error marking notification as read:', error));
}

/**
 * Get schedule time blocks via AJAX
 */
function getTimeBlocks(labId, date) {
    if (!labId || !date) {
        console.error('Lab ID and date are required');
        return;
    }
    
    const url = `/api/schedule/time-blocks?lab_id=${labId}&date=${date}`;
    
    fetch(url)
        .then(response => response.json())
        .then(data => {
            displayTimeBlocks(data.time_blocks);
        })
        .catch(error => console.error('Error fetching time blocks:', error));
}

/**
 * Display time blocks on page
 */
function displayTimeBlocks(blocks) {
    const container = document.getElementById('timeBlocksContainer');
    if (!container) return;
    
    if (blocks.length === 0) {
        container.innerHTML = '<p class="text-muted text-center">No schedules available for this day</p>';
        return;
    }
    
    let html = '<div class="list-group">';
    blocks.forEach(block => {
        const statusColor = block.status === 'Available' ? 'success' : (block.status === 'Reserved' ? 'info' : 'danger');
        html += `
            <div class="list-group-item">
                <div class="d-flex justify-content-between align-items-start">
                    <div>
                        <strong>${block.start_time} - ${block.end_time}</strong>
                        <br>
                        <small class="text-muted">${block.section} - ${block.course}</small>
                    </div>
                    <span class="badge bg-${statusColor}">${block.status}</span>
                </div>
            </div>
        `;
    });
    html += '</div>';
    
    container.innerHTML = html;
}

/**
 * Export table to CSV
 */
function exportTableToCSV(tableId, filename = 'export.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const csvRow = [];
        cols.forEach(col => {
            csvRow.push('"' + col.innerText + '"');
        });
        csv.push(csvRow.join(','));
    });
    
    downloadCSV(csv.join('\n'), filename);
}

/**
 * Download CSV file
 */
function downloadCSV(csv, filename) {
    const csvFile = new Blob([csv], { type: 'text/csv' });
    const downloadLink = document.createElement('a');
    downloadLink.href = URL.createObjectURL(csvFile);
    downloadLink.download = filename;
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

/**
 * Print page content
 */
function printContent(elementId) {
    const printWindow = window.open('', '', 'height=400,width=800');
    const element = document.getElementById(elementId);
    if (!element) return;
    
    printWindow.document.write('<html><head><title>Print</title>');
    printWindow.document.write('<link rel="stylesheet" href="/static/css/style.css">');
    printWindow.document.write('</head><body>');
    printWindow.document.write(element.innerHTML);
    printWindow.document.write('</body></html>');
    printWindow.document.close();
    printWindow.focus();
    printWindow.print();
}

/**
 * Calculate duration between two times
 */
function calculateDuration(startTime, endTime) {
    const start = new Date(`2000-01-01 ${startTime}`);
    const end = new Date(`2000-01-01 ${endTime}`);
    const diff = end - start;
    const hours = Math.floor(diff / 3600000);
    const minutes = Math.floor((diff % 3600000) / 60000);
    return `${hours}h ${minutes}m`;
}

/**
 * Debounce function for search
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Search in table (for client-side filtering)
 */
function searchTable(inputId, tableId) {
    const input = document.getElementById(inputId);
    const table = document.getElementById(tableId);
    if (!input || !table) return;
    
    const filter = input.value.toUpperCase();
    const rows = table.getElementsByTagName('tr');
    
    for (let i = 1; i < rows.length; i++) {
        const row = rows[i];
        const text = row.textContent || row.innerText;
        row.style.display = text.toUpperCase().includes(filter) ? '' : 'none';
    }
}

/**
 * Format bytes to readable format
 */
function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}
