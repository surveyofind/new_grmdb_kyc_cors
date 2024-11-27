$(document).ready(function() {
    function openModal(photoSrc) {
      // Set the source of the enlarged photo in the modal
      $('.enlarged-photo').attr('src', photoSrc);
      
      // Show the modal
      $('.modal-container').fadeIn();
    }
    
    function closeModal() {
      // Hide the modal
      $('.modal-container').fadeOut();
    }
  
    // When the photo is clicked
    $('.photo').on('click', function() {
      // Get the photo source
      const photoSrc = $(this).attr('src');
      openModal(photoSrc);
    });
    
    // When the modal background is clicked
    $('.modal-container').on('click', function(event) {
      // If the clicked element is the background (modal container) itself
      closeModal();
    });
  });