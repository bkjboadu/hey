<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div>
            <div class="p-12 bg-white border border-gray-200 rounded-xl">
                <h1 class="mb-6 text-2xl">Sign Up</h1>

                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem.
                    Lorem ipsum dolor sit mate. Lorem ipsum dolor sit mate. Lorem.
                </p>

                <p class="font-bold">
                   Already have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here </RouterLink> to log in!
                </p>
            </div>
        </div>

        <div>
            <div>
                bright
            </div>
            <div class="p-12 bg-white border border-gray-200 rounded-xl">
                <form class="space-y-4" v-on:submit.prevent="submitForm">
                    <div class="space-y-2">
                        <label class="font-semibold" for="name">Name</label><br>
                        <input class="w-full mt-2 p-4 border border-gray-200 rounded-lg" placeholder="Your Full name" type="text" id="name" v-model="form.name">
                    </div>

                    <div class="space-y-2">
                        <label class="font-semibold" for="industry">industry</label><br>
                        <input class="w-full mt-2 p-4 border border-gray-200 rounded-lg" placeholder="Your industry" type="text" id="industry" v-model="form.industry">
                    </div>
                    
                    <div class="space-y-2">
                        <label class="font-semibold" for="logo">logo</label><br>
                        <input placeholder="password" class="w-full mt-2 p-4 border border-gray-200 rounded-lg" type="file" id="logo" @change="handleFileUpload">
                    </div>

                    <div class="space-y-2">
                        <label class="font-semibold" for="date_founded">date_founded</label><br>
                        <input placeholder="repeat password" v-model="form.date_founded" class="w-full mt-2 p-4 border border-gray-200 rounded-lg" type="date" id="date_founded">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                        </div>
                    </template>

                    <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Register business</button>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import { useToastStore } from '@/stores/toast';
import axios from 'axios'

export default {
    setup() {
        const toastStore = useToastStore()

        return {toastStore}
    },

    data () {
        return {
            form: {
                logo: null,
                name: '',
                industry: '',
                date_founded: ''
            },
            errors: []
        }
    },
    methods: {
        handleFileUpload(event) {
            const file = event.target.files[0];
            this.form.logo = file;
        },
        submitForm () {
            this.errors = []
            if (this.form.name == '') {
                this.errors.push('your name is missing')
            }

            if (this.form.logo == null) {
                this.errors.push('your logo is missing')
            }

            if (this.form.industry == '') {
                this.errors.push('Your industry is missing')
            }

            if (this.form.date_founded == '') {
                this.errors.push('The date_founded does not match')
            }

            if (this.errors.length == 0) {

                const formData = new FormData();

                for (let key in this.form) {
                    formData.append(key,this.form[key])
                }

                formData.append('logo',this.form.logo);

                axios.post('api/business/register-business/', formData)
                .then((response) => {
                    console.log('Response:', response.data);
                    if (response.data.status === 'success') {
                        console.log("It's done")
                        this.toastStore.showToast(5000,'The user is registered. Please log in','bg-emerald-500')
                        this.form.email = ''
                        this.form.name = ''
                        this.form.password1 = ''
                        this.form.password2 = ''

                        this.$router.push('/login')
                    } else {
                        this.toastStore.showToast(5000,'Something went wrong. Please try again','bg-red-300')
                    }
                }) 
                .catch((error) => {
                    console.log('error',error)
                })
            }
        }
    }
}
</script>