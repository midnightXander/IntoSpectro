$(function(){
    const sub_btn = $(".pay-btn");
    const confirm_btn = $("#confirm-btn")
    const pop_up = $("#pop-up-form")
    

//     const sub_btn = document.querySelector("#pay-btn");
//     const confirm_btn = document.querySelector("#confirm-btn")
//     const pop_up = document.querySelector("#pop-up-form")





//    sub_btn.addEventListener("click",(e)=>{
//     var val = e.target.value;
//     console.log(val)
//     confirm_btn.value = val
//     console.log(confirm_btn.value);
//     show_pop_up();

//    })

//    function show_pop_up(){
//     pop_up.style.display = "block";
//     let body =  document.querySelectorAll("section");
//     body.style.opacity = 0.3
//     body.addEventListener("click",()=>{
//         //pop_up.style.display = "none"
//         body.style.opacity = 1
//     })

//    }


   sub_btn.on("click",(e)=>{
   //take the value of the button corresponding to the tier choosed
    var val = $(e.target).attr("value");
    console.log(confirm_btn.attr("value"))
    confirm_btn.attr({
        "value":val,
    }) 
   
    //set the value of confirm button with the clicked tier button 
    $("#sub_id").attr({
        "value":val,
    })
    show_pop_up()

   })

   function show_pop_up(){
    pop_up.show()
    let sections = $("section")
    sections.css("opacity",0.3)
    
    $("#quit").on("click",()=>{
        pop_up.hide()
        sections.css("opacity",1)
    })
   }

})

