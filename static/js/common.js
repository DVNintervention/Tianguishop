document.addEventListener("DOMContentLoaded", function() {
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const textSizeInput = document.getElementById("text-size");

    // Function to update text size
    function updateTextSize(size) {
        document.body.style.fontSize = size + "%";
    }

    // Load and apply text size from local storage
    const storedTextSize = localStorage.getItem("textSize");
    if (storedTextSize) {
        updateTextSize(storedTextSize);
        textSizeInput.value = storedTextSize;
    }

    // Add event listener for text size adjustment
    textSizeInput.addEventListener("input", function() {
        const textSize = this.value;
        updateTextSize(textSize);
        localStorage.setItem("textSize", textSize);
    });

    // Check if the user has a preference for dark mode in local storage
    const isDarkMode = localStorage.getItem("darkMode") === "true";
    if (isDarkMode) {
        document.body.classList.add("dark-mode");
        darkModeToggle.checked = true;
    }

    // Add event listener for dark mode toggle
    darkModeToggle.addEventListener("change", function() {
        document.body.classList.toggle("dark-mode");
        localStorage.setItem("darkMode", darkModeToggle.checked);
    });
});
document.addEventListener("DOMContentLoaded", function() {
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const textSizeInput = document.getElementById("text-size");

    // Function to update text size
    function updateTextSize(size) {
        document.body.style.fontSize = size + "%";
        localStorage.setItem("textSize", size);
    }

    // Check if the user has a preference for dark mode in local storage
    const isDarkMode = localStorage.getItem("darkMode") === "true";
    if (isDarkMode) {
        // Apply dark mode if the preference is true
        document.body.classList.add("dark-mode");
        // Update the checkbox state
        darkModeToggle.checked = true;
    }

    darkModeToggle.addEventListener("change", function() {
        // Toggle 'dark-mode' class on the <body> element
        document.body.classList.toggle("dark-mode");
        // Update the user's preference in local storage
        localStorage.setItem("darkMode", darkModeToggle.checked);
    });

document.addEventListener('DOMContentLoaded', function() {
    // Function to update text size
    function updateTextSize(size) {
        document.body.style.fontSize = size + '%';
    }

    // Load text size from local storage and apply
    const storedTextSize = localStorage.getItem('textSize');
    if (storedTextSize) {
        updateTextSize(storedTextSize);
        document.getElementById('text-size').value = storedTextSize;
    }

    // Event listener for text size adjustment
    document.getElementById('text-size').addEventListener('input', function() {
        const textSize = this.value;
        updateTextSize(textSize);
        localStorage.setItem('textSize', textSize);
    });
});

});