import Foundation

final class AuthService {
    static let shared = AuthService()
    private(set) var accessToken: String?

    func registerDevice() {
        let url = URL(string: "https://api.fitbuddy.example/v1/devices")!
        URLSession.shared.dataTask(with: URLRequest(url: url)) { data, _, _ in
            guard let data = data, let token = String(data: data, encoding: .utf8) else { return }
            print("registered device, access token: \(token)")
            self.accessToken = token
        }.resume()
    }
}
