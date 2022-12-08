$('#open_sidebar').on('click', function(){
    $('.sidebar').css('display', 'block')
    $(this).css('display', 'none')
})

function closeNav(){
    $('.sidebar').css('display', 'none')
    $('#open_sidebar').css('display', 'block')
}