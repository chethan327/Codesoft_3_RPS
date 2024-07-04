document.addEventListener('DOMContentLoaded', function() {
    const choices = document.querySelectorAll('.choice');
    const userChoiceInput = document.getElementById('user-choice');

    choices.forEach(choice => {
        choice.addEventListener('click', function() {
            choices.forEach(c => c.classList.remove('selected'));
            this.classList.add('selected');
            userChoiceInput.value = this.getAttribute('data-choice');
        });
    });

    
    function confirmClose() {
        if (confirm('Are you sure you want to exit?')) {
            window.close();
        }
    }
});
