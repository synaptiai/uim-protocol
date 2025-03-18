// UIM Protocol Documentation Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
  // Initialize custom components
  initializeApiEndpoints();
  initializeCodeCopyButtons();
  initializeVersionSelector();

  // Add scroll animation to anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth'
        });
        history.pushState(null, null, this.getAttribute('href'));
      }
    });
  });
});

// Format API endpoints with method badges
function initializeApiEndpoints() {
  document.querySelectorAll('p').forEach(paragraph => {
    const text = paragraph.textContent;
    const apiEndpointMatch = text.match(/^(GET|POST|PUT|DELETE|PATCH)\s+(\S+)/);

    if (apiEndpointMatch) {
      const method = apiEndpointMatch[1];
      const url = apiEndpointMatch[2];

      // Create new elements
      const apiEndpoint = document.createElement('div');
      apiEndpoint.className = 'api-endpoint';

      const methodSpan = document.createElement('span');
      methodSpan.className = `api-method ${method.toLowerCase()}`;
      methodSpan.textContent = method;

      const urlSpan = document.createElement('span');
      urlSpan.className = 'api-url';
      urlSpan.textContent = url;

      // Replace paragraph with new elements
      apiEndpoint.appendChild(methodSpan);
      apiEndpoint.appendChild(urlSpan);

      paragraph.parentNode.replaceChild(apiEndpoint, paragraph);
    }
  });
}

// Add copy buttons to code blocks
function initializeCodeCopyButtons() {
  document.querySelectorAll('pre > code').forEach(codeBlock => {
    // Check if copy button already exists
    if (!codeBlock.parentNode.querySelector('.copy-button')) {
      const button = document.createElement('button');
      button.className = 'copy-button';
      button.textContent = 'Copy';

      button.addEventListener('click', () => {
        navigator.clipboard.writeText(codeBlock.textContent).then(() => {
          button.textContent = 'Copied!';
          setTimeout(() => {
            button.textContent = 'Copy';
          }, 2000);
        });
      });

      codeBlock.parentNode.appendChild(button);
    }
  });
}

// Initialize version selector
function initializeVersionSelector() {
  const versionSelector = document.querySelector('.md-version');

  if (versionSelector) {
    // Add event listener to version selector
    versionSelector.addEventListener('change', (event) => {
      const version = event.target.value;
      window.location.href = `/${version}/`;
    });
  }
}
