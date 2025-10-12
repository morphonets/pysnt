// Complete navbar customization and theme toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    // Wait for the navbar to be fully loaded
    setTimeout(function() {
        const navbar = document.querySelector('.bd-navbar .bd-navbar__inner');
        
        if (navbar) {
            // Find the logo (should be first child)
            const logo = navbar.querySelector('.navbar-brand');
            
            // Create center navigation
            const centerNav = document.createElement('ul');
            centerNav.className = 'navbar-nav navbar-center-nav';
            centerNav.innerHTML = `
                <li class="nav-item">
                    <a class="nav-link" href="install.html">
                        <i class="fas fa-download"></i> Install
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="notebooks/index.html">
                        <i class="fas fa-book"></i> Notebooks
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://imagej.net/plugins/snt/" target="_blank">
                        <i class="fas fa-question-circle"></i> Ask a Question
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://imagej.net/plugins/snt/contribute" target="_blank">
                        <i class="fas fa-hands-helping"></i> Contribute
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="https://imagej.net/plugins/snt/" target="_blank">
                        <i class="fas fa-book-open"></i> SNT User Manual
                    </a>
                </li>
            `;
            
            // Create right navigation
            const rightNav = document.createElement('ul');
            rightNav.className = 'navbar-nav navbar-right-nav';
            rightNav.innerHTML = `
                <li class="nav-item">
                    <a class="nav-link" href="https://github.com/morphonets/pysnt" target="_blank" title="GitHub Repository">
                        <i class="fab fa-github"></i>
                    </a>
                </li>
                <li class="nav-item">
                    <button class="btn nav-link theme-switch-button" id="theme-switch" title="Switch between light and dark mode">
                        <i class="fas fa-sun" id="theme-icon"></i>
                    </button>
                </li>
            `;
            
            // Clear existing navbar content except logo
            const existingNavs = navbar.querySelectorAll('.navbar-nav');
            existingNavs.forEach(nav => nav.remove());
            
            // Add our custom navigation
            if (logo) {
                navbar.insertBefore(centerNav, logo.nextSibling);
                navbar.appendChild(rightNav);
            } else {
                navbar.appendChild(centerNav);
                navbar.appendChild(rightNav);
            }
            
            // Initialize theme functionality
            initializeTheme();
        }
    }, 200);
    
    function initializeTheme() {
        const themeSwitch = document.getElementById('theme-switch');
        const themeIcon = document.getElementById('theme-icon');
        const body = document.body;
        
        if (!themeSwitch || !themeIcon) return;
        
        // Check for saved theme preference or default to 'light'
        const currentTheme = localStorage.getItem('theme') || 'light';
        
        // Apply the saved theme
        if (currentTheme === 'dark') {
            body.setAttribute('data-theme', 'dark');
            themeIcon.className = 'fas fa-moon';
        } else {
            body.setAttribute('data-theme', 'light');
            themeIcon.className = 'fas fa-sun';
        }
        
        // Theme switch event listener
        themeSwitch.addEventListener('click', function() {
            const currentTheme = body.getAttribute('data-theme');
            
            if (currentTheme === 'dark') {
                body.setAttribute('data-theme', 'light');
                themeIcon.className = 'fas fa-sun';
                localStorage.setItem('theme', 'light');
            } else {
                body.setAttribute('data-theme', 'dark');
                themeIcon.className = 'fas fa-moon';
                localStorage.setItem('theme', 'dark');
            }
        });
    }
});