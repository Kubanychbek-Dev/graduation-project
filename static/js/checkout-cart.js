$(".checkout__btn-pay").on("click", function() {
  let userPhone = $(".checkout__recipient_phone").text()
  let userAddress = $(".checkout__recipient-address").text().trim()
  let subtotal = parseFloat($("#cart-subtotal").val().replace(",", "."))

  $.ajax({
    url: "/checkout",
    data: {
      "phone": userPhone,
      "address": userAddress,
      "subtotal": subtotal
    },
    dataType: "json",
    beforeSend: function() {
      console.log("Sending")
    },
    success: function(response) {
      if(response) {
        console.log(response.success_url)
        const fullUrl = window.location.protocol + "//" + window.location.hostname + ":8000" + "/" + "checkout_success/" + response.success_url
        window.location.assign(fullUrl)
      }
    }
  })
})