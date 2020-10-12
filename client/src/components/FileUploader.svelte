<script lang="ts">
  let files: string[] | Blob[];
  let hexCode = "";
 
  async function handleSubmit() {
    if (files.length > 0) {
      const formData = new FormData();
      formData.append("file", files[0]);
      const response = await fetch("http://0.0.0.0:8000/color/what", {
        method: "POST",
        body: formData
      }).then((response) => {
        return response.json();
      });

      hexCode = response.color;
    }
  }
</script>

{#if !hexCode}
<form on:submit|preventDefault={handleSubmit}>
  <input required id="file" type="file" bind:files />
  <input type="submit" value="Upload file" />
</form>
{/if}


{#if hexCode}
<div class="box" style="background-color:{hexCode}">
    {hexCode}
</div>
{/if}

<style>
    .box {
        width: 100px;
        height: 100px;
        border: 1px solid #000;
    }
</style>

