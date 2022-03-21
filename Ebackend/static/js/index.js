function displayLink(){
    let links= document.querySelector('.buyer-seller')
    if (links.style.display === 'none'){
        links.style.display = 'flex';
    }
    else{
        links.style.display = 'none'
    }

}