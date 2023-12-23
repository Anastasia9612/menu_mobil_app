function getFormattedDateRange(weekNumber) {
    var today = new Date();
    var startDay = new Date(today);
    var endDay = new Date(today);
  
    startDay.setDate(today.getDate() - today.getDay() + (weekNumber - 1) * 7 + 1);
    endDay.setDate(startDay.getDate() + 6);
  
    var formattedFirstDay = startDay.toLocaleDateString('en-GB', { day: 'numeric', month: 'numeric' }).replace(/\//g, '.');
    var formattedLastDay = endDay.toLocaleDateString('en-GB', { day: 'numeric', month: 'numeric' }).replace(/\//g, '.');
  
    var formattedDateRange = formattedFirstDay + '-' + formattedLastDay;
    return formattedDateRange;
  }
  document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn[data-week="1"]').innerText = getFormattedDateRange(1);
    document.querySelector('.btn[data-week="2"]').innerText = getFormattedDateRange(2);
  });



  document.addEventListener('DOMContentLoaded', function() {
    showWeek(2);
    showWeek(1);
  });
  function showWeek(weekNumber) {
    //скрываем все дни обеих недель
    $(".day").hide();
    //показываем выбранную неделю
    $(".week" + weekNumber).show();
  
    //Удаляем класс у всех кнопок
    $(".btn").removeClass("selected-week");
    //Добавляем класс выбранной кнопке недели
    $(".btn[data-week='" + weekNumber + "']").addClass("selected-week");
  
    // Скрываем дни первой недели, если выбрана вторая неделя
    if (weekNumber === 2) {
      $(".week1 .weekdays").hide();
    } else {
      $(".week1 .weekdays").show();
    }
    //Наоборот
    if (weekNumber === 1) {
      $(".week2 .weekdays").hide();
    } else {
      $(".week2 .weekdays").show();
    }
    // Обновляем текст кнопок дней недели с учетом выбранной недели
    var startDay = getStartDayOfTheWeek(weekNumber); // Получаем дату начала недели
  
    var daysOfWeek = ["Вс", "Пн", "Вт", "Ср", "Чт", "Пт", "Сб"];
    $(".week" + weekNumber + " .weekdays button").each(function(index) {
      var currentDate = new Date(startDay.getFullYear(), startDay.getMonth(), startDay.getDate() + index);
      var dayNumber = currentDate.getDate();
      var dayName = daysOfWeek[currentDate.getDay()]; // Получаем наименование дня недели
      $(this).html('<div>' + dayNumber + '</div><div>' + dayName + '</div>'); // Обновляем содержимое кнопки
    });
  }
  function getStartDayOfTheWeek(weekNumber) {
    var today = new Date();
    var dayOfWeek = today.getDay() - 1; // Получаем день недели (0 - воскресенье, 1 - понедельник, и т.д.)
    var diff = today.getDate() - dayOfWeek + (weekNumber - 1) * 7; // Вычисляем разницу для корректного начала недели
    var startDate = new Date(today.getFullYear(), today.getMonth(), diff); // Создаем новую дату с учетом разницы
    
    return startDate;
  }
      function showDay(dayNumber) {
      $(".day").hide();
      $("#day" + dayNumber).show();
    }
  
    $(document).ready(function () {
      $(".btn-outline-success").on("click", function () {
        $(".btn-outline-success").removeClass("active");
        $(this).addClass("active");
      });
    });
