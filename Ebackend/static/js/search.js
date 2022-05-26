token= document.cookie.split('=')[1]
const searchProd= ()=>{
    let searchInput= document.querySelector('[name=search-term')
    let searchIcon= document.querySelector('.fa-magnifying-glass')

    searchIcon.addEventListener('click', (e)=>{
        searchItem= searchInput.value

        searchInput.value= ''

        if(searchItem){
            fetch('search/', {
                method: 'POST',
                body: JSON.stringify(searchItem),
                'headers': {
                    'Content-Type': 'application/json',
                    'X-CSRFToken' : token

                }
            })//end fetch
            .then((response)=>{
                return response.json()
            })
            .then((searchdata)=>{
                console.log(searchdata)
            })
        }
    })
}

searchProd()