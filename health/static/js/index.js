let con = document.getElementById("myContactForm");
con.addEventListener("submit", (e) => {
  e.preventDefault();
    Swal.fire(
        {
            title: "Thank you for contacting!",
            text: "We will reach out to you as soon as possible.",
            icon: "success",
            confirmButtonText: "Close",
            confirmButtonColor: "#007bff",
            closeOnConfirm: true,
        },
        function (isConfirm) {
            if (isConfirm) con.submit();
        }
        
    );
    // setTimeout(() => { window.location.reload() }, 2000);
});

// $(document).ready(function () {
//     $('#btn-submit').click(function (e) {
//         let $form = $(this).closest('form');

//         const swalWithBootstrapButtons = Swal.mixin({
//             customClass: {
//                 confirmButton: 'btn btn-success',
//                 cancelButton: 'btn btn-danger'
//             },
//             buttonsStyling: false,
//         })

//         swalWithBootstrapButtons.fire({
//             title: 'Are you sure?',
//             text: "Check plz",
//             type: 'warning',
//             showCancelButton: true,
//             confirmButtonText: 'OK',
//             cancelButtonText: 'Cancel',
//             reverseButtons: true
//         }).then((result) => {
//             if (result.value) {
//                 swalWithBootstrapButtons.fire(
//                     'Finished',
//                     'Success',
//                     'success',
//                 );
//                 $form.submit();
//             } else if (
//                 result.dismiss === Swal.DismissReason.cancel
//             ) {
//                 swalWithBootstrapButtons.fire(
//                     'Cancelled',
//                     'Do corrections and then retry :)',
//                     'error'
//                 );
//             }
//         });

//     });
// })