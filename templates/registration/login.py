{% extends 'registration/registration_base.html' %}
{% block title %}Dj Learning Management System - Login{% endblock title %}
{% load crispy_forms_tags %}
{% block content %}

<div class="col-md-4 mx-auto mt-5">
  <div class="card">
    <div class="form-title">
      <i class="fas fa-lock me-2"></i>
      Sign in
    </div>
    <div class="card-body">
        <form action="" method="POST" id="login-form">{% csrf_token %}
          <div class="form-group mb-3">
              <label class="mb-2" for="username_id"><i class="fas fa-address-card me-2"></i>ID Number</label>
              <input type="text" name="username" id="username_id" class="form-control" required>
              <div id="message-wrapper"></div>
          </div>
          <div class="form-group mb-3">
              <label class="mb-2" for="password_id"><i class="fas fa-key me-2"></i>Password</label>
              <input type="password" name="password" id="password_id" class="form-control" required>
          </div>
          {% if form.errors %}
                <span class="text-danger"><i class="fas fa-exclamation-circle"></i> Invalid ID & Password.</span><br>
          {% endif %}
      
          <button type="submit" class="btn btn-primary" id="login-btn"><i class="fas fa-sign-in-alt"></i><small> SIGN IN</small></button>
        </form>
        <br>
        <div class="login-bottom">
          <a href="{% url 'password_reset' %}" class="link">Forgot password ?</a>
          <a href="{% url 'password_reset' %}" class="link"> Sign up</a>
        </div>
      </div>
  </div>
</div>
{% endblock content %}

{% block js %}

<script>
  $('#login-form').submit(function (e) {
    // e.preventDefault();
    $('#login-btn').addClass('disabled')
    $('#login-btn').html(`<i class="fas fa-sign-in-alt"></i> Signining you in . . .`)
  })

  $("#username").on("input", function () {
    username = $(this).val();

    $.ajax({
      url: "/accounts/ajax/validate-username/",
      data: {
        username: username
      },
      dataType: 'json',
      success: function (data) {
        if (data.is_taken) {
          console.log(data.is_taken);
          $('#message-wrapper').html(`<p class="my-2 text-danger"><span class="bg-error p-2"><b>${username}</b> already taken :( try another one </span></p>`)
        }
        else {
          $('#message-wrapper').html(`<p class="my-2 text-success"><span class="bg-correct p-2"><b>${username}</b> is valid </span></p>`)
        }
      }

    })
  })
</script>
{% endblock %}
