// Notification System JavaScript
class NotificationSystem {
    constructor() {
        this.notifications = [];
        this.isVisible = false;
        this.currentNotification = null;
        this.init();
    }

    init() {
        this.createNotificationContainer();
        this.loadNotifications();
        this.setupEventListeners();
        this.startPolling();
    }

    createNotificationContainer() {
        // Create overlay
        this.overlay = document.createElement('div');
        this.overlay.className = 'notification-popup-overlay';
        this.overlay.style.display = 'none';

        // Create popup
        this.popup = document.createElement('div');
        this.popup.className = 'notification-popup';
        this.popup.style.display = 'none';

        // Add to body
        document.body.appendChild(this.overlay);
        document.body.appendChild(this.popup);
    }

    setupEventListeners() {
        // Close button
        this.overlay.addEventListener('click', () => this.hideNotification());
        
        // Prevent popup click from closing
        this.popup.addEventListener('click', (e) => e.stopPropagation());
    }

    async loadNotifications() {
        try {
            const response = await fetch('/notifications/api/unread/');
            if (response.ok) {
                const data = await response.json();
                this.notifications = data.notifications || [];
                console.log('Loaded notifications:', this.notifications);
                this.showNextNotification();
            } else {
                console.error('Failed to load notifications:', response.status);
            }
        } catch (error) {
            console.error('Error loading notifications:', error);
        }
    }

    showNextNotification() {
        console.log('showNextNotification called. isVisible:', this.isVisible, 'notifications count:', this.notifications.length);
        if (this.isVisible || this.notifications.length === 0) {
            console.log('Not showing notification. isVisible:', this.isVisible, 'notifications count:', this.notifications.length);
            return;
        }

        this.currentNotification = this.notifications.shift();
        console.log('Showing notification:', this.currentNotification);
        this.displayNotification(this.currentNotification);
    }

    displayNotification(notification) {
        if (!notification) return;

        this.isVisible = true;
        
        // Create notification HTML
        const priorityClass = notification.priority || 'medium';
        const priorityText = this.getPriorityText(notification.priority);
        const sentDate = new Date(notification.sent_date || notification.created_at);
        const timeString = sentDate.toLocaleString('ar-SA', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });

        this.popup.innerHTML = `
            <div class="notification-popup-header">
                <h4>
                    <i class="bi bi-bell me-2"></i>
                    ${notification.title}
                </h4>
                <button class="notification-popup-close" onclick="notificationSystem.hideNotification()">
                    <i class="bi bi-x"></i>
                </button>
            </div>
            <div class="notification-popup-body">
                <div class="notification-popup-message">
                    ${notification.message}
                </div>
                <div class="notification-popup-meta">
                    <span class="notification-priority ${priorityClass}">
                        ${priorityText}
                    </span>
                    <span class="notification-popup-time">
                        <i class="bi bi-clock me-1"></i>
                        ${timeString}
                    </span>
                </div>
                <div class="notification-popup-actions">
                    <button class="notification-popup-btn notification-popup-btn-success" onclick="notificationSystem.markAsRead(${notification.id})">
                        <i class="bi bi-check-circle me-1"></i>
                        تمييز كمقروء
                    </button>
                    <button class="notification-popup-btn notification-popup-btn-primary" onclick="notificationSystem.viewDetails(${notification.id})">
                        <i class="bi bi-eye me-1"></i>
                        عرض التفاصيل
                    </button>
                    <button class="notification-popup-btn notification-popup-btn-secondary" onclick="notificationSystem.hideNotification()">
                        <i class="bi bi-x-circle me-1"></i>
                        إغلاق
                    </button>
                </div>
            </div>
        `;

        // Show notification
        this.overlay.style.display = 'block';
        this.popup.style.display = 'block';

        // Auto-hide after 10 seconds for non-urgent notifications
        if (notification.priority !== 'urgent') {
            setTimeout(() => {
                if (this.isVisible) {
                    this.hideNotification();
                }
            }, 10000);
        }
    }

    hideNotification() {
        this.isVisible = false;
        this.overlay.style.display = 'none';
        this.popup.style.display = 'none';
        
        // Show next notification after a short delay
        setTimeout(() => {
            this.showNextNotification();
        }, 1000);
    }

    async markAsRead(notificationId) {
        try {
            const response = await fetch(`/notifications/${notificationId}/mark-read/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': this.getCSRFToken(),
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                this.hideNotification();
                this.updateNotificationCount();
            }
        } catch (error) {
            console.error('Error marking notification as read:', error);
        }
    }

    viewDetails(notificationId) {
        window.location.href = `/notifications/${notificationId}/`;
    }

    getPriorityText(priority) {
        const priorities = {
            'low': 'منخفض',
            'medium': 'متوسط',
            'high': 'عالي',
            'urgent': 'عاجل'
        };
        return priorities[priority] || 'متوسط';
    }

    getCSRFToken() {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            const [name, value] = cookie.trim().split('=');
            if (name === 'csrftoken') {
                return value;
            }
        }
        return '';
    }

    updateNotificationCount() {
        // Update notification count in header if exists
        const countElement = document.querySelector('.notification-count');
        if (countElement) {
            const currentCount = parseInt(countElement.textContent) || 0;
            countElement.textContent = Math.max(0, currentCount - 1);
        }
    }

    startPolling() {
        // Check for new notifications every 30 seconds
        setInterval(() => {
            if (!this.isVisible) {
                this.loadNotifications();
            }
        }, 30000);
    }

    // Public method to show notification manually
    showNotification(notification) {
        this.notifications.unshift(notification);
        if (!this.isVisible) {
            this.showNextNotification();
        }
    }
}

// Initialize notification system when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.notificationSystem = new NotificationSystem();
});

// Function to show notification from server-side
function showServerNotification(notification) {
    if (window.notificationSystem) {
        window.notificationSystem.showNotification(notification);
    }
}
