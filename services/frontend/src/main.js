import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from './store';

import "./assets/style/tailwind.css";
import "./assets/style/global.css";
import axios from "axios";

// import { predictComponent } from "./utils/import";

const app = createApp(App);

// predictComponent(app);

axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000/';

app.use(router);
app.use(store);
app.mount("#app");
