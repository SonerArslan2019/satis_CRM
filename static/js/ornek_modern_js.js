document.addEventListener('DOMContentLoaded', function () {
    // Kapı tiplerini alma
    const kapi_tipi_div = document.getElementById('div_id_kapi_tipi');
    // Diğer div'ler için aynı yöntemle tanımlamalar yapılabilir
    // ...

    let selected_door = '';

    const doors = [
        // doors dizisi aynı kalabilir
    ];

    // Elementleri gizleme
    function hideElement(element) {
        if (element) element.style.display = 'none';
    }

    hideElement(kapi_tipi_div);
    // Diğer div'ler için de aynı fonksiyonu kullanabilirsiniz
    // ...

    // Kapı tiplerini alma
    let door_name_list = doors.map(door => door.name);

    // Yeni bir select box oluşturma
    let door_name = kapi_tipi_div.cloneNode(true);
    door_name.id = 'door_name';
    door_name.querySelector('select').name = 'door_name';
    kapi_tipi_div.parentNode.insertBefore(door_name, kapi_tipi_div.nextSibling);
    kapi_tipi_div.style.display = 'none';

    // Select box doldurma işlemleri
    let selectElement = door_name.querySelector('select');
    selectElement.innerHTML = door_name_list.map(door => `<option value="${door}">${door}</option>`).join('');

    selectElement.addEventListener('change', function () {
        // İlgili işlemler
    });

    // Diğer event listener'lar ve fonksiyonlar
    // ...
});
