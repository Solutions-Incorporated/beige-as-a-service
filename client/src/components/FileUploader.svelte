<script>
  let files;
  let statusCode = "";
 
  async function handleSubmit() {
    if (files.length > 0) {
      const formData = new FormData();
      formData.append("file", files[0]);
      const response = await fetch("/color/what", {
        method: "POST",
        body: formData
      });
      statusCode = response.status;
    }
  }
</script>
 
{statusCode}
<form on:submit|preventDefault={handleSubmit}>
  <label for="file">File</label>
  <input required id="file" type="file" bind:files />
  <input type="submit" value="Upload file" />
</form>