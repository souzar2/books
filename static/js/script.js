var myModal = new bootstrap.Modal(document.getElementById('staticBackdrop'));

// Quando o botão para abrir o modal é clicado
document.querySelectorAll('[data-bs-toggle="modal"]').forEach(function(button) {
  button.addEventListener('click', function() {
    var email = this.getAttribute('data-email'); // Obtém o valor do atributo de dados 'data-email'
    var modalBody = document.querySelector('.modal-body');
    modalBody.textContent = 'Email do Livro: ' + email; // Insere o email no corpo do modal
    myModal.show(); // Abre o modal
  });
});