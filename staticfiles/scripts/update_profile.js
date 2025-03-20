document.addEventListener('DOMContentLoaded', function() {
    const avatarInput = document.getElementById('avatarInput');
    const avatarPreview = document.getElementById('avatarPreview');
    const removePictureBtn = document.getElementById('removeAvatarBtn');
    // const profilePicture = document.getElementById('profilePicture');
    const removeAvatarInput = document.getElementById('removeAvatarInput');

    avatarInput.addEventListener('change', function(e) {
        if (this.files && this.files[0]) {
            const reader = new FileReader();
            
            reader.onload = function(e) {
                avatarPreview.src = e.target.result;
            }
            
            reader.readAsDataURL(this.files[0]);
        }
    });

    removePictureBtn.addEventListener('click', function(e) {
        console.log('Remove button clicked'); 
        e.preventDefault();
        // Clear the file input
        avatarInput.value = '';
        // Set the profile picture to the default SVG image
        avatarPreview.src = '/static/media/avatars/default.svg'; // Adjust the path as needed
        // Set the hidden input to indicate removal
        removeAvatarInput.value = 'true';
    });
});