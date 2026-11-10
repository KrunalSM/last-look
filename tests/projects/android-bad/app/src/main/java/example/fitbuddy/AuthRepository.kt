package example.fitbuddy

import android.util.Log

object AuthRepository {
    var token: String? = null

    fun onLoginSuccess(newToken: String) {
        Log.d("Auth", "login ok, token=$newToken")
        token = newToken
    }

    fun logout() {
        token = null
    }
}
