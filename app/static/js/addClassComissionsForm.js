  // Función para agregar clases a los elementos
function addClassesToForm() {
    // Agregar clase al formulario
    var form = document.querySelector('form');
    form.classList.add('my-form');

    // Agregar clase "mb-3" a las etiquetas <li>
    var listItems = document.querySelectorAll('li');
    listItems.forEach(function (li, index) {
      li.classList.add('mb-3');
      // Si es la primera etiqueta <li>, agregar clase "form-control" al input
      if (index === 0) {
        var inputField = li.querySelector('input');
        if (inputField) {
          inputField.classList.add('form-control');
        }
      }
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

    // Agregar clases a los campos de entrada (input) que no estén en el primer <li>
    var inputFields = document.querySelectorAll('li:not(:first-child) input');
    inputFields.forEach(function (field) {
      field.classList.add('form-select');
    });

    // Agregar clase al botón de submit
    var submitButton = document.querySelector('button[type="submit"]');
    submitButton.classList.add('my-button');
  }

  // Llamar a la función cuando el contenido del DOM esté cargado
document.addEventListener('DOMContentLoaded', function () {
  addClassesToForm();
});
