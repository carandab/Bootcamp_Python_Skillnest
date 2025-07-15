$(document).ready(function () {
  const $thumbnails = $('.thumbnail');
  const modalElement = document.getElementById('imageModal');
  const $modalImg = $('#modal-img');
  const $modalDesc = $('#modal-description');
  const modal = new bootstrap.Modal(modalElement);
  let currentIndex = 0;

  function showImage(index) {
    const $img = $($thumbnails[index]);
    const src = $img.attr('src');
    const desc = $img.data('description') || '';

    $modalImg.attr('src', src);
    $modalDesc.text(desc);
    currentIndex = index;
    modal.show();
  }

  $thumbnails.click(function () {
    const index = $thumbnails.index(this);
    showImage(index);
  });

  $('#next').click(function () {
    currentIndex = (currentIndex + 1) % $thumbnails.length;
    showImage(currentIndex);
  });

  $('#prev').click(function () {
    currentIndex = (currentIndex - 1 + $thumbnails.length) % $thumbnails.length;
    showImage(currentIndex);
  });

  // Manejar con el teclado
  $(document).keydown(function (e) {
    if (!modalElement.classList.contains('show')) return; // Solo si modal está abierto

    if (e.key === "Escape") {
      modal.hide();
    } else if (e.key === "ArrowRight") {
      $('#next').click();
    } else if (e.key === "ArrowLeft") {
      $('#prev').click();
    }
  });
});


// Efecto hover
$('.thumbnail').on('mouseenter', function () {
  $(this).css({
    transform: 'scale(1.05)',
    zIndex: 2,
    transition: 'transform 0.3s ease'
  });
});

$('.thumbnail').on('mouseleave', function () {
  $(this).css({
    transform: 'scale(1)',
    zIndex: 1
  });
});
