$(document).ready(function() {

    $('.first').hide()
    $('.second').hide()
    $('.third').hide()
    $('.fourth').hide()
    $('.fifth').hide()
    $('.sixth').hide()
    $('.seventh').hide()
    $('.eighth').hide()

    let medicinal = [];

    console.log(medicinal)
    $('.btn').on('click', function() {
        $('.pitchwrap').fadeOut(350)
        $('.btn').fadeOut(350)
        $('.first').fadeIn(1000)
    })

    $('.yes1').on('click', function() {
        if (medicinal.length !== 1) {
            medicinal.push("t")
        }
        $('.no1').hide()
        $('.first').fadeOut(300).promise().done(function() {
            $('.second').fadeIn(1000)
        })
    })
    $('.no1').on('click', function() {
        if (medicinal.length !== 1) {
            medicinal.push("f")
        }
        $('.yes1').hide()
        $('.first').fadeOut(300).promise().done(function() {
            $('.second').fadeIn(1000)
        })
    })
    $('.yes2').on('click', function() {
        if (medicinal.length !== 2) {
            medicinal.push("t")
        }
        $('.no2').hide()
        $('.second').fadeOut(300).promise().done(function() {
            $('.third').fadeIn(1000)
        })
    })
    $('.no2').on('click', function() {
        if (medicinal.length !== 2) {
            medicinal.push("f")
        }
        $('.yes2').hide()
        $('.second').fadeOut(300).promise().done(function() {
            $('.third').fadeIn(1000)
        })
    })
    $('.yes3').on('click', function() {
        if (medicinal.length !== 3) {
            medicinal.push("t")
        }
        $('.no3').hide()
        $('.third').fadeOut(300).promise().done(function() {
            $('.fourth').fadeIn(1000)
        })
    })
    $('.no3').on('click', function() {
        if (medicinal.length !== 3) {
            medicinal.push("f")
        }
        $('.yes3').hide()
        $('.third').fadeOut(300).promise().done(function() {
            $('.fourth').fadeIn(1000)
        })
    })
    $('.yes4').on('click', function() {
        if (medicinal.length !== 4) {
            medicinal.push("t")
        }
        $('.no4').hide()
        $('.fourth').fadeOut(300).promise().done(function() {
            $('.fifth').fadeIn(1000)
        })
    })
    $('.no4').on('click', function() {
        if (medicinal.length !== 4) {
            medicinal.push("f")
        }
        $('.yes4').hide()
        $('.fourth').fadeOut(300).promise().done(function() {
            $('.fifth').fadeIn(1000)
        })
    })
    $('.yes5').on('click', function() {
        if (medicinal.length !== 5) {
            medicinal.push("t")
        }
        $('.no5').hide()
        $('.fifth').fadeOut(300).promise().done(function() {
            $('.sixth').fadeIn(1000)
        })
    })
    $('.no5').on('click', function() {
        if (medicinal.length !== 5) {
            medicinal.push("f")
        }
        $('.yes5').hide()
        $('.fifth').fadeOut(300).promise().done(function() {
            $('.sixth').fadeIn(1000)
        })
    })
    $('.yes6').on('click', function() {
        if (medicinal.length !== 6) {
            medicinal.push("t")
        }
        $('.no6').hide()
        $('.sixth').fadeOut(300).promise().done(function() {
            $('.seventh').fadeIn(1000)
        })
    })
    $('.no6').on('click', function() {
        if (medicinal.length !== 6) {
            medicinal.push("f")
        }
        $('.yes6').hide()
        $('.sixth').fadeOut(300).promise().done(function() {
            $('.seventh').fadeIn(1000)
        })
    })
    $('.yes7').on('click', function() {
        if (medicinal.length !== 7) {
            medicinal.push("t")
        }
        $('.no7').hide()
        $('.seventh').fadeOut(300).promise().done(function() {
            $('.eighth').fadeIn(1000)
        })
    })
    $('.no7').on('click', function() {
        if (medicinal.length !== 7) {
            medicinal.push("f")
        }
        $('.yes7').hide()
        $('.seventh').fadeOut(300).promise().done(function() {
            $('.eighth').fadeIn(1000)
        })
    })
    $('.yes8').unbind('on')
    $('.yes8').on('click', function() {
        if (medicinal.length !== 8) {
            medicinal.push("t")
        }
        med = JSON.stringify(medicinal)
        console.log(med)
        $('.valyes').val(med)
        console.log($('.valyes').attr("value"))
        $('.no8').hide()
        $('.eighth').fadeOut(300)
    })
    $('.no8').unbind('on')
    $('.no8').on('click', function() {
        if (medicinal.length !== 8) {
            medicinal.push("f")
        }
        med = JSON.stringify(medicinal)
        console.log(med)
        $('.valno').val(med)
        console.log($('.valno').attr("value"))
        $('.yes8').hide()
        $('.eighth').fadeOut(300)
    })
    $('.sub1').on('click', function() {
        $('.f1').submit()
        return false
    })
    $('.sub2').on('click', function() {
        $('.f2').submit()
        return false
    })
})