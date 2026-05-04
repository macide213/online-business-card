/* 
  Redesigned script.js 
  Since update_vcard.py handles the data generation, 
  this script can stay minimal or handle UI feedback.
*/

document.addEventListener('DOMContentLoaded', () => {
    console.log('Digital Business Card Loaded');
    
    // Add subtle click effect to buttons
    const buttons = document.querySelectorAll('.contact-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            btn.style.transform = 'scale(0.95)';
            setTimeout(() => btn.style.transform = '', 100);
        });
    });
});
