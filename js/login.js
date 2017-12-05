/**
 * @class Vue component 
 * @author ritesh.patel 
 * @email ritesh@line89.com 
 * @since 12/04/2017
 * @description Vue component for the VrtxApp
 */
let vrtxApp = new Vue({
    el: '#vrtxapp',
    // instance data
    data: {
        email: Cookies.get('email') || '',
        password: '',
        token: Cookies.get('token') || '',
        hasToken: (Cookies.get('token') && Cookies.get('token').length > 0) || false,
        name: '',
        price: '',
        instruments: '<tr><td class="text-center" colspan=3><i class="fa fa-spinner fa-spin"></i>&nbsp;loading...</td></tr>'
    },
    // instance methods
    methods: {
        /**
         * @method init
         * Initialization 
         */
        init: function () {
            // keep user in the app if token has been established
            console.log('token ', this.hasToken);
            if (this.hasToken) {
                this.getListing();
            }
        },

        /**
         * @method login 
         * Processes login, this route is exempted from the middleware 
         */
        login: function () {
            if (this.email && this.password) {
                // make jquery request to login endpoint
                $.ajax({
                    url: 'api/login',
                    type: 'POST',
                    data: JSON.stringify({email: this.email, password: this.password}),
                    contentType: 'application/json',
                    success: function (response) {
                        if (response.status === 'success') {
                            Cookies.set('email', this.email);
                            Cookies.set('token', response.data);
                            this.token = response.data;
                            this.hasToken = true;
                            this.getListing();
                        } else {
                            alert('Error logging into VrtxApp');
                        }
                    }.bind(this),
                    error: function (err) {

                    }.bind(this)
                })
            }
        },

        /**
         * @method getListing 
         * Returns instrument listing
         */
        getListing: function () {
            $.ajax({
                type: "GET",
                url: 'api/instruments',
                contentType: 'application/json',
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('Authorization', this.token)
                }.bind(this),
                success: function (response) {
                    var data, 
                        key,
                        value,
                        list = '',
                        k;
                    if (response.status === 'success') {
                        data = response.data;

                        for (k in data) {
                            value = data[k];
                            list += '<tr><td><input type="checkbox" name="cb" value="' + k + '"><td>' + k + '</td><td>' + value + '</td></tr>';
                        }
                        this.instruments = list;
                    } else {
                        alert('Error loading data...')
                    }
                }.bind(this),
                error: function (err) {

                }.bind(this)
            })
        },

        /**
         * @method logout 
         * Mimics logout. Clears token and displays login div
         */
        logout: function () {
            if (confirm('Are you sure you wish to logout?')) {
                this.token = '';
                this.hasToken = false;

                // clear cookies
                Cookies.remove('token');
                Cookies.remove('email');
            }
        },

        /**
         * @method addInstrument 
         * Adds a new instrument
         */
        addInstrument: function () {
            if (this.name && this.price) {
                var data = {'name': this.name, 'price': this.price}
                $.ajax({
                    url: 'api/instruments',
                    method: 'POST',
                    data: JSON.stringify({name: this.name, price: this.price}),
                    contentType: 'application/json',
                    beforeSend: function (xhr) {
                        xhr.setRequestHeader('Authorization', this.token)
                    }.bind(this),                    
                    success: function (response) {
                        var data,
                            key,
                            value,
                            list = '';

                        if (response.status === 'success') {
                            data = response.data;
                            this.getListing();        
                            this.name = '';
                            this.price = '';                  
                        } else {
                            alert('Error adding instrument');
                        }
                    }.bind(this),
                    error: function (err) {
                        // display error
                    }.bind(this)
                })
            }
        },
        /**
         * @method remove instrument
         */
        deleteInstrument: function () {
            var cb = document.querySelectorAll('input[name=cb]:checked'),
                arr = [], 
                remove = {},
                i = 0,
                len = cb.length;

            for (i = 0; i < len; i++) {
                remove = {};
                remove.name = cb[i].value;
                arr.push(remove);
            }


        }
    }
});

// keep user in the app if token has been established
vrtxApp.init();