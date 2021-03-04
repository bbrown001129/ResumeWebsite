function viewPopUp(element) {
    var instruction = document.getElementById(element);
    if (instruction.style.display == 'block') {
        instruction.style.display = 'none';
    }
    else {
        instruction.style.display = 'block';
    }
    
}