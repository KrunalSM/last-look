import { useEffect, useState } from "react";
import { Text, View } from "react-native";
import { Camera } from "expo-camera";
import * as Location from "expo-location";
import * as Notifications from "expo-notifications";

export default function App() {
  const [place, setPlace] = useState("locating...");

  useEffect(() => {
    (async () => {
      await Camera.requestCameraPermissionsAsync();
      await Notifications.requestPermissionsAsync();
      const { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") return;
      const here = await Location.getCurrentPositionAsync({});
      console.log("current position", here.coords.latitude, here.coords.longitude);
      setPlace(`${here.coords.latitude.toFixed(2)}, ${here.coords.longitude.toFixed(2)}`);
    })();
  }, []);

  return (
    <View>
      <Text>TrailNotes</Text>
      <Text>You are near {place}</Text>
    </View>
  );
}
