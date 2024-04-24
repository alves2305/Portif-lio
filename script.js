let cardVisible = false;

// Oculta o cartão quando a página é carregada
document.addEventListener("DOMContentLoaded", function() {
    let card = document.querySelector(".card");
    card.style.display = "none";
});

function clicar() {
    let card = document.querySelector(".card");

    if (cardVisible) {
        card.style.display = "none";
        cardVisible = false;
    } else {
        card.style.display = "block"; // ou "flex", dependendo do estilo do elemento
        cardVisible = true;
    }
}
