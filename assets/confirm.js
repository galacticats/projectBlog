function confirmDelete(){
    var wantToDelete = confirm("Are you sure you want to delete your account and ALL of your posts?");
    if (!wantToDelete){
        event.preventDefault();
    }
}