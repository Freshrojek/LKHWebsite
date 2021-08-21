// import Vue from 'vue'
// import Router from 'vue-router'

// import Blog from '@/components/pages/Blog'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/blog',
            name: 'Blog',
            component: Blog
        }
    ]
})