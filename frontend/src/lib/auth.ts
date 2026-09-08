import Cookies from "js-cookie";
import api from "./api";

export interface LoginPayload {
  username: string;
  password: string;
}

export interface RegisterPayload {
  email: string;
  username: string;
  password: string;
  first_name: string;
  last_name: string;
  role: "CLIENT" | "PROVIDER";
}

export async function login(payload: LoginPayload) {
  const { data } = await api.post("/auth/login/", payload);
  Cookies.set("access_token", data.access, { expires: 1 });
  Cookies.set("refresh_token", data.refresh, { expires: 7 });
  return data;
}

export async function register(payload: RegisterPayload) {
  const { data } = await api.post("/auth/register/", payload);
  return data;
}

export function logout() {
  Cookies.remove("access_token");
  Cookies.remove("refresh_token");
}

export async function getMe() {
  const { data } = await api.get("/auth/me/");
  return data;
}