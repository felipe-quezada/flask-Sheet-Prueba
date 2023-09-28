const currentData = () => {
	fetch('/list', { method: 'GET' })
		.then((res) => res.json())
		.then((data) => {
			let areaSelect = document.querySelector('#table');
			let printer = '';
			data.forEach(
				(el) =>
					(printer += `
      <tr>
        <th>${el.id}</th>
        <td>${el.nombre}</td>
        <td>${el.edad}</td>
        <td>${el.profesion}</td>
      </tr>`)
			);
			areaSelect.innerHTML = printer;
		})
		.catch((err) => console.error(err));
};
