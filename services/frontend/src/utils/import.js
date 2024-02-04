import { defineAsyncComponent } from "vue";

export function predictComponent(app) {
    app.component("auth-layout", defineAsyncComponent(() => import("@/layouts/auth-layout.vue")));
    app.component("default-layout", defineAsyncComponent(() => import("@/layouts/default-layout.vue")));
}
