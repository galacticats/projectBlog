//Grab the title input field and the slug input field
const titleField = document.querySelector('input[name=title]');
const slugField = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g,'-'); // \s is spaces, \W is non word
};

//Create an event listener for when the user types into the title
titleField.addEventListener('keyup', (e) => {
    slugField.setAttribute('value', slugify(titleField.value));
});