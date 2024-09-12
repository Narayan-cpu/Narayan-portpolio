// portfolio_app/static/portfolio_app/script.js

// Typing animation
const typingText = document.querySelector('.typing-text');
const phrases = ["a Web Developer.", "a Software Engineer.", "a Problem Solver."];
let phraseIndex = 0;
let letterIndex = 0;
let currentText = "";
let isDeleting = false;

function type() {
    if (isDeleting) {
        currentText = phrases[phraseIndex].substring(0, letterIndex - 1);
        letterIndex--;
        if (letterIndex === 0) {
            isDeleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
        }
    } else {
        currentText = phrases[phraseIndex].substring(0, letterIndex + 1);
        letterIndex++;
        if (letterIndex === phrases[phraseIndex].length) {
            isDeleting = true;
        }
    }
    typingText.textContent = currentText;
    setTimeout(type, isDeleting ? 100 : 200);
}

// Scroll animation for projects
function revealProjectsOnScroll() {
    const projects = document.querySelectorAll('.project');
    projects.forEach((project) => {
        const projectTop = project.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (projectTop < windowHeight - 50) {
            project.classList.add('visible');
        }
    });
}

// Initialize typing animation
window.addEventListener('load', () => {
    type();
});

// Scroll event for project reveal
window.addEventListener('scroll', revealProjectsOnScroll);
