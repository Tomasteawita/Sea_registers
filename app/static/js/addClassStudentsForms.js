
// Función para agregar clases a los elementos
function addClassesToForm() {
// Agregar clase al formulario
var form = document.querySelector('form');
form.classList.add('my-form');

// Agregar clase "form-control" a todos los campos de entrada (inputs)
var inputFields = form.querySelectorAll('input');
inputFields.forEach(function (field) {
    field.classList.add('form-control');
});

// Agregar clases a las etiquetas label
var labels = document.querySelectorAll('label');
labels.forEach(function (label) {
    label.classList.add('my-label');
});

// Agregar clase "form-select" a las etiquetas <select>
var selectFields = document.querySelectorAll('select');
selectFields.forEach(function (select) {
    select.classList.add('form-select');
});

// Agregar clase al botón de submit
var submitButton = document.querySelector('button[type="submit"]');
submitButton.classList.add('my-button');
}

// Llamar a la función cuando el contenido del DOM esté cargado
document.addEventListener('DOMContentLoaded', function () {
addClassesToForm();
  });
