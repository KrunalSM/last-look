import AVFoundation
import Contacts
import CoreLocation
import UIKit
import UserNotifications

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
    let locationManager = CLLocationManager()

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        AVCaptureDevice.requestAccess(for: .video) { _ in }
        locationManager.requestWhenInUseAuthorization()
        CNContactStore().requestAccess(for: .contacts) { _, _ in }
        UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound]) { _, _ in }
        AuthService.shared.registerDevice()
        return true
    }
}
