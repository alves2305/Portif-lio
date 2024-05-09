

// Oculta o cartão quando a página é carregada
document.addEventListener("DOMContentLoaded", function() {
    let card = document.querySelector(".card");
    card.style.display = "none";
});

let cardVisible = false;

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


function abrirArquivos() {
    // URL do primeiro arquivo (currículo)
    const curriculoURL = "arquivos/curriculo.pdf";
    
    // URL do segundo arquivo (certificado)
    const certificadoURL = "arquivos/certificado.pdf";

    // Abrir uma nova aba para o currículo
    window.open(curriculoURL, '_blank');

    // Abrir uma nova aba para o certificado
    window.open(certificadoURL, '_blank');
}


document.addEventListener("DOMContentLoaded", function() {
    let card2 = document.querySelector(".form-container");
    card2.style.display = "none";
});


let cardFormVisible = false;
function cardForm(){
    let clique = document.querySelector(".form-container");

    if (cardFormVisible) {
        clique.style.display = "none"
        cardFormVisible = false; 
    } else {
        clique.style.display = "flex"
        cardFormVisible = true;
    }

}




