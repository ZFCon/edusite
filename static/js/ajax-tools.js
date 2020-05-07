function ButtonWrapper(buttonObj) {
    this.originText = $(buttonObj).text();

    this.loading = function() {
        $(buttonObj).attr('disabled', true);
        $(buttonObj).html('<span class="spinner-border spinner-border-sm"></span> Loading...');
    }

    this.reset = function() {
        $(buttonObj).text(this.originText);
        $(buttonObj).attr('disabled', false);
    }
}