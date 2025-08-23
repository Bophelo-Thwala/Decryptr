export interface UserProfile {
    id: String,
    username: String,
    email: String,
    password: String,
    photo: String,
    provider: 'google' | 'local'
}