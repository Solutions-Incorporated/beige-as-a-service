<script lang="ts">
  let files: string[] | Blob[];
  let color = "";
 
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

      color = response.color;
    }
  }
</script>
 
{color}

<form on:submit|preventDefault={handleSubmit}>
  <label for="file">File</label>
  <input required id="file" type="file" bind:files />
  <input type="submit" value="Upload file" />
</form>