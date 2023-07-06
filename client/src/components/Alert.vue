<template>
  <div>
    <div class="alert alert-success alert-dismissible" role="alert">
      {{ message }}
      <button
        type="button"
        class="btn-close"
        data-bs-dismiss="alert"
        aria-label="Close"
        @click="closeClicked"
      ></button>
    </div>
    <br />
  </div>
</template>   

<script>
export default {
  props: ["message"],
  methods: {
    closeClicked() {
      this.$emit("closeAlertEvent");
    },
  },
};
</script>