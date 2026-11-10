package example.fitbuddy

import android.os.Bundle
import android.widget.Button
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity

class SettingsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val column = LinearLayout(this).apply { orientation = LinearLayout.VERTICAL }
        column.addView(Button(this).apply { text = "Change password" })
        column.addView(Button(this).apply {
            text = "Log out"
            setOnClickListener { AuthRepository.logout(); finish() }
        })
        setContentView(column)
    }
}
