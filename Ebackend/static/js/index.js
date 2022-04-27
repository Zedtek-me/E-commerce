// display quick links
function displayLink(){
    let links= document.querySelector('.b-seller')
    let arrowDown= document.querySelector('.fa-angle-down')
    links.classList.toggle('buyer-seller')
    arrowDown.classList.toggle('fa-angle-down')
    arrowDown.classList.toggle('fa-angle-up')
}


// "how it works"--> a hover effect that displays how a product works
const howItWorks= ()=>{
    let detail= document.querySelector('.detail')
    let detailParent= document.querySelector('.how-it-works')
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

// details about the cart functionality
const cartDetail= ()=>{
    var addToCart= document.querySelectorAll('.add-to-cart')//the add to cart parent
    var cart_detail= document.querySelectorAll('.cart-detail')//the details when hover 
    for(let j= 0; j<addToCart.length; j++){
        addToCart[j].addEventListener('mouseover', (e)=>{
            cart_detail[j].style.display='flex';
            setTimeout(()=>{cart_detail[j].style.display='none'}, 5000)})
            };
}
cartDetail()

// remove cart item button at the index page
const removeCartItem= ()=>{
    let removeCart= document.querySelectorAll('.remove-cart')
    let cart_count= document.querySelector('.cart-count')
    let cartForm= document.querySelectorAll('.cart-form')
    for(let j= 0; j<removeCart.length; j++){
        removeCart[j].addEventListener('click',(e)=>{
            cart_count.textContent=Number(cart_count.textContent)-1;//first, deduct 1 from the cart count.
            if(cart_count.textContent == 0){//if the count is deducted down to Zero, assign an empty string instead of 0
                cart_count.textContent= ''
            }
            const formInfo= new FormData(cartForm[j])
            fetch('/remove_from_cart/', {
                method:'POST',
                body: formInfo
            })
            .then((response)=>{console.log(response)})
            removeCart[j].style.display='none'//remove the button
        })
        
    }
}
removeCartItem()

// add to cart implementation
const cartCount= ()=>{
    let addToCart= document.querySelectorAll('.add-to-cart')/*the add to cart parent */
    let cart_count= document.querySelector('.cart-count')/*the cart content container--> increases in number when an item is added to cart*/
    let removeCart= document.querySelectorAll('.remove-cart')/*remove item from cart button */
    let cartForm= document.querySelectorAll('.cart-form')
    for(let j= 0; j<addToCart.length; j++){
        addToCart[j].addEventListener('click', (e)=>{
            // get product data when cart button is clicked;
            formInfo= new FormData(cartForm[j])
            // send data to backend for storage, and display at checkout.
            fetch('/add_to_cart/', {
                method:'POST',
                body: formInfo
            })
            cart_count.textContent=Number(cart_count.textContent)+1;
            removeCart[j].style.display='flex';
            })
        }
}
cartCount()

// get the total of products selected
const totalAmount = ()=>{
    let productPrice = document.querySelectorAll('#p-price')
    let quantity = document.querySelectorAll('#quantity-tag')//the quantity elements
    let total= document.querySelector('.total')
    sum= 0
    for( let i= 0; i< productPrice.length; i++){
        sum += Number(productPrice[i].textContent.split('Price: $')[1])
    }
    total.textContent +=`$${sum}.0`
}
totalAmount()

// increase or decrease the amount of product to be purchased
const increaseNdDecreaseAmount= ()=>{
    let productPrice = document.querySelectorAll('#p-price')
    let quantity = document.querySelectorAll('#quantity-tag')
    let total= document.querySelector('.total')
    for (let j= 0; j< quantity.length; j++){
        let initialProductPrice= Number(productPrice[j].innerText.split('Price: $')[1])// inital price of the product which will be multiplied by the quantity provided.
        let initialQuantity= Number(quantity[j].value)//tracking the initial state(or quantity) of the product, to identify increase/decrease
        quantity[j].addEventListener('change', (e)=>{
            if(Number(e.target.value > initialQuantity))//this means an increase in quantity
            {
                initialQuantity = Number(e.target.value)
                productPrice[j].innerText= `Price: $${initialProductPrice * Number(e.target.value)}`
                total.innerText= `Total: $${Number(total.innerText.split('Total: $')[1]) + initialProductPrice}.0`
            }
            else if(Number(e.target.value < initialQuantity))//this means a decrease in quantity
            {
                initialQuantity = Number(e.target.value)
                productPrice[j].innerText= `Price: $${initialProductPrice * Number(e.target.value)}`
                total.innerText= `Total: $${Number(total.innerText.split('Total: $')[1]) - initialProductPrice}.0`
            }
        })//event listener ends here
    }
}

increaseNdDecreaseAmount()