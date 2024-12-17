// script.js
document.getElementById('whatsappForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    if (!phone || !message) {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    // Monta o link para o WhatsApp
    const whatsappLink = `https://wa.me/+55${phone}?text=${encodeURIComponent(message)}`;

    // Redireciona para o WhatsApp
    window.open(whatsappLink, '_blank');
});
